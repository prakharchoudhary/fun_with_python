import webbrowser

class Movie():
	def __init__(self, title, poster, bio, trailer):
		self.title = title
		self.poster_image_url = poster
		self.storyline = bio
		self.trailer_youtube_url = trailer

def show_trailer(self):
	webbrowser.open(self.trailer_url)