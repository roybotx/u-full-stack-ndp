from media import Movie
from fresh_tomatoes import open_movies_page

""" This file is to create 3 different movies and load to the webpage. """

avengers = Movie("Avengers 2",
                 "https://www.youtube.com/watch?v=tmeOjFno6Do",
                 "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg")
ip_man = Movie("Ip Man 3",
                 "https://www.youtube.com/watch?v=yo7z8c87Egg",
                 "https://upload.wikimedia.org/wikipedia/en/3/3a/IpMan3.jpg")
rush_hour = Movie("Rush Hour 3",
                 "https://www.youtube.com/watch?v=CJUwvbECRI0",
                 "https://upload.wikimedia.org/wikipedia/en/4/44/Rushhour3poster.jpg")

movies = [avengers, ip_man, rush_hour]
open_movies_page(movies)
