import webbrowser


# Created a Movie class to supply the movie data
class Movie():
    # Constructor method that applies movie title,
    # movie storyline, poster image and Youtube Trailer
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        # Every instance called has a parameter of movie title,
        # movie storyline, poster image, and youtube trailer
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # Everytime play_trailer is called,
        # this method helps the the Trailer modal display the trailer

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

