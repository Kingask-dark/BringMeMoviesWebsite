
# BringMeMoviesWebsite 

  Bring Me Movies is a Movie Recommendation System developed in Django.

## Installation

Install BringMeMoviesWebsite

```bash
  git clone https://github.com/Kingask-dark/BringMeMoviesWebsite
  cd BringMeMoviesWebsite
  pip install -r requirements.txt
```
## Neccessary Configuration
  Before running the project you will need to do:
  1) Extract similarity.zip file from Templates/BringMeMovies/main/
  2) Create your account in https://www.themoviedb.org/ and generate your api key and put it in fetch_posters function in views.py file 
  3) Provide the full path of movies.pkl and similarity.pkl files located in Templates/BringMeMovies/main/ in the views.py file

## Run
  To Run BringMeMoviesWebsite:

```bash
    cd BringMeMoviesWebsite
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```
## Screenshots

![Project Screenshots](/static/images/HomePage.png?raw=true "HomePage")
![Project Screenshots](/static/images/Login.png?raw=true "LoginPage")
![Project Screenshots](/static/images/SignUp.png?raw=true "SignUpPage")
![Project Screenshots](/static/images/RecommendedMovies.png?raw=true "RecommendedMovies")
![Project Screenshots](/static/images/RecommededForYou.png?raw=true "RecommededForYou")


## Author

- [@Kingask-dark](https://github.com/Kingask-dark)

