import webbrowser


class Movie ():
    """ Class for representing a movie """

    def __init__(
            self,
            movie_title,
            movie_storyline,
            movie_poster,
            movie_trailer):
        """ Initiate a Movie object
        Args:
        movie_title = a string of the movie's title.
        movie_storyline = a string of the movie's storyline.
        movie_poster = a string containing a URL to a movie poster.
        movie_trailer = a string containing a youtube URL of the movie's
        trailer.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """ Open trailer in a web browser """
        webbrowser.open(self.trailer_youtube_url)
