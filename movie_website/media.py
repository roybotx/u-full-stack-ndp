import webbrowser

class Movie:
    """ Movie class. """
    def __init__(self, title, trailer_url, image_url):
        self.title = title
        self.trailer_youtube_url = trailer_url
        self.poster_image_url = image_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
