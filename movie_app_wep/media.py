import webbrowser

class Movie():
    """ this class provides a way to store move related information"""
    
    VAR_RATINGS=["PG","R"]
	
    def __init__(self, movie_title, movie_storyline, poster_image,
		trailer_youtube):
	self.title = movie_title
	self.storyline = movie_storyline
	self.poster_image_url = poster_image
	self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
	webbrowser.open(self.trailer_youtube_url)
