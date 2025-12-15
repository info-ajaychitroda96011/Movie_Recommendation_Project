import streamlit as st
import pickle
import pandas as pd
import  requests


movie_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

options = movie_list.to_dict('index')

selected_movie_name = st.selectbox("Select Movie",
                      list(options.items()),
                      format_func=lambda item:item[1]['title'])

def fetched_movie_name(t):
    return t[1]['title']

title = fetched_movie_name(selected_movie_name)

def recommend(movie):
    movie_index = movie_list[movie_list['title']== movie].index[0]
    distance = similarity[movie_index]
    movies = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movie = []
    recommended_movie_poster = []
    for i in movies:
        movie_id = movie_list.iloc[i[0]].movie_id
        recommended_movie.append(movie_list.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_image(movie_id))
    return recommended_movie,recommended_movie_poster



def fetch_image(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6ce0b8c9c2b7fb16379b98f2bef4ced5&language=en-US'.format(movie_id))

    data = response.json()

    return "http://image.tmdb.org/t/p/w500"+data['poster_path']

if st.button('Search'):
    name,poster = recommend(title)
    
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])

