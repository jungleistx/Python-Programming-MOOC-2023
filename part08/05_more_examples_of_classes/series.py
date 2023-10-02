# Write your solution here:

class Series:
	def __init__(self, title:str, seasons:int, genres:list):
		self.title = title
		self.seasons = seasons
		self.genres = genres
		self.ratings = 0
		self.score = 0

	def __str__(self):
		genre_str = ", ".join(self.genres)
		if self.ratings > 0:
			rating = f"{self.ratings} ratings, average {self.score/self.ratings:.1f} points"
		else:
			rating = 'no ratings'
		return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_str}\n{rating}"

	def rate(self, rating:int):
		if rating >= 0 and rating <= 5:
			self.ratings += 1
			self.score += rating


def minimum_grade(rating:float, series_list:list):
	over_rating_list = []
	for serie in series_list:
		if serie.ratings > 0:
			serie_grade = serie.score / serie.ratings
			if serie_grade >= rating:
				over_rating_list.append(serie)
	return over_rating_list


def includes_genre(genre:str, series_list:list):
	genre_included = []
	for serie in series_list:
		if genre in serie.genres:
			genre_included.append(serie)
	return genre_included


# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# print(dexter)

# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# dexter.rate(4)
# dexter.rate(5)
# dexter.rate(5)
# dexter.rate(3)
# dexter.rate(0)
# print(dexter)
# print()

# s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# s1.rate(5)

# s2 = Series("South Park", 24, ["Animation", "Comedy"])
# s2.rate(3)

# s3 = Series("Friends", 10, ["Romance", "Comedy"])
# s3.rate(2)

# series_list = [s1, s2, s3]

# print("a minimum grade of 4.5:")
# for series in minimum_grade(4.5, series_list):
#     print(series.title)

# print("genre Comedy:")
# for series in includes_genre("Comedy", series_list):
#     print(series.title)
