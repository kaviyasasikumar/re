from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



app = Flask(__name__)

# Load movie data
movies = pd.read_csv('movies.csv')

# Combine features
movies['combined'] = movies['genre'] + ' ' + movies['description']

# Vectorize
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movies['combined'])

# Similarity matrix
similarity = cosine_similarity(tfidf_matrix)

def recommend(movie_name):
    if movie_name not in movies['title'].values:
        return ["Movie not found."]
    
    idx = movies[movies['title'] == movie_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    recommendations = [movies.iloc[i[0]]['title'] for i in scores]
    return recommendations

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        movie = request.form['movie']
        recommendations = recommend(movie)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '_main_':
    app.run(debug=True)
app = Flask(__name__)

# Load movie data
movies = pd.read_csv('movies.csv')

# Combine features
movies['combined'] = movies['genre'] + ' ' + movies['description']

# Vectorize
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movies['combined'])

# Similarity matrix
similarity = cosine_similarity(tfidf_matrix)

def recommend(movie_name):
    if movie_name not in movies['title'].values:
        return ["Movie not found."]
    
    idx = movies[movies['title'] == movie_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    recommendations = [movies.iloc[i[0]]['title'] for i in scores]
    return recommendations

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        movie = request.form['movie']
        recommendations = recommend(movie)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '_main_':
    app.run(debug=True)
app = Flask(__name__)

# Load movie data
movies = pd.read_csv('movies.csv')

# Combine features
movies['combined'] = movies['genre'] + ' ' + movies['description']

# Vectorize
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movies['combined'])

# Similarity matrix
similarity = cosine_similarity(tfidf_matrix)

def recommend(movie_name):
    movie_name_lower = movie_name.lower()
    movie_titles_lower = movies['title'].str.lower()

    matches = movie_titles_lower[movie_titles_lower == movie_name_lower]
    if matches.empty:
        return ["Movie not found."]
    
    idx = matches.index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_movies = [movies.iloc[i[0]].title for i in scores]
    return recommended_movies

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        movie = request.form['movie']
        recommendations = recommend(movie)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)