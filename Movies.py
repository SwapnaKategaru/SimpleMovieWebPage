import webbrowser


class Movie:

    # init creates space in memory to take arguments of which the function self is first which point towards specific
    # movie referred from a collection of movies followed by the instance variables
    def __init__(self, movie_title, movie_story_line, movie_poster_image, movie_show_trailer):
        """
        :param movie_title: title of movie
        :param movie_story_line: story of movie
        :param movie_poster_image: poster image of movie
        :param movie_show_trailer: youtube trailer of movie
        """
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = movie_poster_image
        self.show_trailer_url = movie_show_trailer

    # defining function(show_trailer) plays specified movie trailers which happens through self
    def show_trailer(self):
        """
        web browser.open helps to open link or url from instance variable.show_trailer_url
        """
        webbrowser.open(self.show_trailer_url)
