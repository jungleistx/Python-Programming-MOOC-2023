# Write your solution here

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
	new_movie = {}
	new_movie['name'] = name
	new_movie['director'] = director
	new_movie['year'] = year
	new_movie['runtime'] = runtime

	database.append(new_movie)


if __name__ == "__main__":
	database = []
	add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
	add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
	print(database)