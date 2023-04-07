import streamlit as st
import pickle
import pandas as pd
import numpy as np

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity_cosine = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distances = similarity_cosine[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    ratings = []

    for i in movies_list:
        movie_id = i[0]
        
        
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching poster from dataset itself
        posters_path = "http://image.tmdb.org/t/p/w185" + movies.iloc[movie_id].poster_path
        recommended_movies_poster.append(posters_path)
        
        # ratings
        rating = movies.iloc[movie_id].vote_average
        ratings.append(rating)
    return recommended_movies,recommended_movies_poster, ratings
   

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Which movie you want to choose?',
movies['title'].values)


#def show(selected_movie_name):
    #detail.text('Ratings: {}'.format(ratings))



if st.button('Recommend'):
    names,posters,rate = recommend(selected_movie_name)
    #for i in recommendations:
        #st.write(i)
    col1 , col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
        st.text('IMDB ratings : ')
        st.text(rate[0])
        
   
        
    with col2:
        st.text(names[1])
        st.image(posters[1])
        st.text('IMDB ratings : ')
        st.text(rate[1])
        
    with col3:
        st.text(names[2])
        st.image(posters[2])
        st.text('IMDB ratings : ')
        st.text(rate[2])
        
    with col4:
        st.text(names[3])
        st.image(posters[3])
        st.text('IMDB ratings : ')
        st.text(rate[3])
        
    with col5:
        st.text(names[4])
        st.image(posters[4])
        st.text('IMDB ratings : ')
        st.text(rate[4])