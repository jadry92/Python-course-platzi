import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
			"lalala", 
			"http://img.lum.dolimg.com/v1/images/open-uri20150422-7119-1406xde_4feee003.jpeg", 
			"https://www.youtube.com/watch?v=JcpWXaA2qeg")

toy_story_1 = media.Movie("Toy Story", 
			"lalala", 
			"http://img.lum.dolimg.com/v1/images/open-uri20150422-7119-1406xde_4feee003.jpeg", 
			"https://www.youtube.com/watch?v=JcpWXaA2qeg")
toy_story_2 = media.Movie("Toy Story", 
			"lalala", 
			"http://img.lum.dolimg.com/v1/images/open-uri20150422-7119-1406xde_4feee003.jpeg", 
			"https://www.youtube.com/watch?v=JcpWXaA2qeg")
toy_story_3 = media.Movie("Toy Story", 
			"lalala", 
			"http://img.lum.dolimg.com/v1/images/open-uri20150422-7119-1406xde_4feee003.jpeg", 
			"https://www.youtube.com/watch?v=JcpWXaA2qeg")
toy_story_4 = media.Movie("Toy Story", 
			"lalala", 
			"http://img.lum.dolimg.com/v1/images/open-uri20150422-7119-1406xde_4feee003.jpeg", 
			"https://www.youtube.com/watch?v=JcpWXaA2qeg")
toy_story_5 = media.Movie("Toy Story", 
			"lalala", 
			"http://img.lum.dolimg.com/v1/images/open-uri20150422-7119-1406xde_4feee003.jpeg", 
			"https://www.youtube.com/watch?v=JcpWXaA2qeg")
toy_story_6 = media.Movie("Toy Story", 
			"lalala", 
			"http://img.lum.dolimg.com/v1/images/open-uri20150422-7119-1406xde_4feee003.jpeg", 
			"https://www.youtube.com/watch?v=JcpWXaA2qeg")
movies = [toy_story, toy_story_1, toy_story_2, toy_story_3, toy_story_4, toy_story_5, toy_story_6]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
print(media.Movie.__bases__)

