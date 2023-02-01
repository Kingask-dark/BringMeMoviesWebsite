from django.shortcuts import render, redirect
from BringMeMovies.models import SearchedMovies
import pickle
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import pandas as pd
from itertools import chain
import requests

movies = pickle.load(open(
    'Enter the full path of movie.pkl file which is located in Templates/BringMeMovies/main', 'rb'))
similarity = pickle.load(open(
    'Enter the full path of similarity.pkl file which is located in Templates/BringMeMovies/main', 'rb'))
Movies = pd.DataFrame(movies)

def fetch_poster(movieId):
    res = requests.get((f'https://api.themoviedb.org/3/movie/{movieId}?api_key=<<Enter your Api Key>>&language=en-US'))
    data = res.json()
    return "https://image.tmdb.org/t/p/w154/"+data['poster_path']


def BringMeMovies(movie):
    movie_index = Movies[Movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    SimilarMoviesList = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = []
    Poster = []
    Genres = []
    for similarMovies in SimilarMoviesList:
        recommended.append(Movies.iloc[similarMovies[0]].title)
        Poster.append(fetch_poster(Movies.iloc[similarMovies[0]].id))
        Genres.append(Movies.iloc[similarMovies[0]].genres)
    return recommended , Poster , Genres

def Home(req):
    if not req.user.is_authenticated:
        return redirect('/login/')
    else:
        moviesList = Movies['title'].values
        searchedText = req.POST.get('SearchMovie')
        data = list(SearchedMovies.objects.filter(user_name=req.user).values('Serchmovie'))
        databaseData = []
        if req.method == 'POST':
            for movvvv in data:
                databaseData.append(movvvv['Serchmovie'])
            if searchedText not in databaseData:
                if searchedText in moviesList:
                    searchedMovies = SearchedMovies(Serchmovie=searchedText ,user_name = User.objects.get(id=req.user.id))
                    searchedMovies.save()
        
        history = list(SearchedMovies.objects.filter(user_name=req.user).values('Serchmovie'))
        RecommendedMoviesForYou = []
        reccmm = []
        recmm = []
        recPoster = []
        RecGenres = []
        for moviee in history:
            recmm ,recPos,resGenres = BringMeMovies(moviee['Serchmovie'])
            reccmm.append(recmm)
            recPoster.extend(recPos)
            RecGenres.extend(resGenres)
        RecommendedMoviesForYou = list(chain.from_iterable(reccmm))
        rec = []
        recposter = []
        SearchRecGenres = []
        buttonClick = req.POST.get('Bring')
        if(buttonClick):
            if searchedText in moviesList:
                reccom , reccomPos,SearchGenres = BringMeMovies(searchedText)
                rec.extend(reccom)
                recposter.extend(reccomPos)
                SearchRecGenres.extend(SearchGenres)
        return render(req, 'BringMeMovies/html/Homepage.html', {'SearchRecommended': rec, 'RecommendedMovies': RecommendedMoviesForYou,
         'MovieList': moviesList ,'Poster':recposter ,'RecommendedPoster':recPoster ,'Genres':RecGenres,'SearchRecGenres':SearchRecGenres,'searchedText':searchedText})


def Login(req):
    if req.method == 'POST':
        userName = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=userName, password=password)
        if user is not None:
            login(req, user)
            return redirect('/')
        else:
            messages.error(req, "User or Password is wrong")
            return redirect('/login/')
    return render(req, "BringMeMovies/html/LoginPage.html")


def Signup(req):
    if req.method == "POST":
        fName = req.POST['fname']
        lName = req.POST['lname']
        userName = req.POST['username']
        email = req.POST['email']
        password1 = req.POST['password1']
        password2 = req.POST['password2']
        myUser = User.objects.create_user(userName, email, password2)
        myUser.first_name = fName
        myUser.last_name = lName
        myUser.save()
        messages.success(req, "Your Account Has Been Created Successfully.")
        return redirect('/login/')

    return render(req, "BringMeMovies/html/SignupPage.html")


def logOut(req):
    logout(req)
    messages.success(req, "logout successfully")
    return redirect('/login/')
