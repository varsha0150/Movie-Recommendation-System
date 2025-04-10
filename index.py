import streamlit as st 
import pickle

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movies_list = movies['title'].values

st.header("Movie Recommendation System")
sel_val= st.selectbox("Select movie" , movies_list)


def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distance= sorted(list(enumerate(similarity[index])) , reverse=True , key=lambda  vector:vector[1])
    recommend_movie=[]
    for i in distance[0:10]:
      recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie  


if st.button("Show Recommendations"):
    reccomendations = recommend(sel_val)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
       st.text(reccomendations[0])
    with col2:
       st.text(reccomendations[1])
    with col3:
       st.text(reccomendations[2])
    with col4:
       st.text(reccomendations[3])
    with col5:
       st.text(reccomendations[4])            