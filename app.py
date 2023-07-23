import streamlit as st
import pickle
import pandas as pd
import requests
# here we define a function which we provide the movie_id and it hit the api for which we require a library named as "requests"


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ea2b67fab0d2041bd7af2f50d1ba5c07&language=en-US'.format(movie_id))
    data=response.json()
    # st.text(data)
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']

def recommended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies= []
    recommended_movies_posters=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('moviedict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title('movie Recommender System')

# option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))
#
# st.write('You selected:', option)

# like that we have to show the recommendation of movies for which we can use pickle library

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    names,posters=recommended(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])

#  for deployment we need to make 4 files(procfile and a setup.sh for directories,git ignore,a list of