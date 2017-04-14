# Project : Movie Trailer Website
## By  Fouad Asharf



## Table of contents
- [Description](#description)
- [Required Libraries and Dependencies](#required-libraries-and-dependencies)
- [How to Run Project](#how-to-run-project)
- [Project contents](#project-contents)

- [Copyright and license](#copyright-and-license)
 
## Description
This is a simple movie trailer website which displays a listing of favorite movies and links each movie to its trailer's video on YouTube ,this project is a part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Required Libraries and Dependencies

Python 2.x is required to run this project , you can download it from https://www.python.org/downloads/.

## How to Run Project

Download the project zip file to you computer and unzip the file. Or clone this repository to your desktop using the terminal window in Linux or the command prompt in Windows and type the following command:
```bash
git clone https://github.com/fouad3/movie_trailer_udacity_project.git
```
Navigate to the project directory using the following command:


```
cd movie_trailer_udacity_project
```
Run main Python script [entertainment_center.py](https://github.com/fouad3/movie_trailer_udacity_project/blob/master/entertainment_center.py) using the following command:

```bash
python entertainment_center.py
```

Your default browser should launch a new tab displaying the movie trailer website.

## Project contents



#### Movie object class

The Movie object class consists of four class variables, a simple constructor method, and a class method for playing a Movie object's movie trailer. The code is located in [media.py](https://github.com/fouad3/movie_trailer_udacity_project/blob/master/media.py). 

##### constructor method

The constructor method is called when a new Movie object is created and must include four arguments  [movie-title](#movie-title), [movie-storyline](#movie-storyline), [movie-poster](#movie-poster), and [movie_trailer](#movie-trailer). Each of these arguments is discussed further below.

```bash
import media

#information for object arguments
movie-title = "Manchester by the Sea"
movie-storyline = "A depressed uncle is asked to take care of his teenage nephew after 
the boy's father dies.."
movie-poster = "http://www.impawards.com/2016/posters/manchester_by_the_sea.jpg"
movie_trailer = "https://www.youtube.com/watch?v=gsVoD0pTge0"

# Create Movie object
manchester_by_the_sea = media.Movie(movie-title, movie-storyline, movie-poster, movie_trailer)
```

###### movie-title

movie-title is a string used to identify the movie object.

###### movie-storyline

movie-storyline is a string represent the story of the movie. 

###### movie-poster

movie-poster is a string containing a URL linking to an image which will be used to represent the Movie object.

###### movie-trailer

movie.trailer_url is a string containing a URL linking to the movie trailer on YouTube.

###### show_trailer method

show_trailer can be called on any Movie class object to launch that object's movie trailer in a webpage. This method is useful for testing but is not used by the script that generates the finished movie trailers page.

### Movie Trailer Page Functions 

The functions used to create the final movie trailers page are located in [fresh_tomatoes.py](https://github.com/fouad3/movie_trailer_udacity_project/blob/master/fresh_tomatoes.py), along with HTML template variables used by these functions. This file must be imported to access the functions described below.

#### open_movies_page function

To create the static movie trailers page the open_movies_page function must be called and supplied with one required argument (an array of Movie class objects).

```bash
# Create movie trailer page with array of Movie class objects
movies = [
    movie1,
    movie2,
    movie3]
fresh_tomatoes.open_movies_page(movies)

``` 

## Copyright and License

- supplied without rights information contributed by [Udacity](http://www.udacity.com).
