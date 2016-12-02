import media
import make_website

toy_story = media.Movie("Toy Story", "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg", "Story of a boy and his toys that come to life", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#add more such movies with all related info to make the site look even better

movies = [toy_story]
#enter the movies in the array

make_website.open_movies_page(movies)

