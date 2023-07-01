# Write your solution here

def read_recipe_file(filename:str) -> dict:
	recipes = {}
	with open(filename) as file:
		is_recipe_name = True
		for line in file:
			line = line.replace('\n', '')
			if is_recipe_name:
				recipe_name = line
				recipes[recipe_name] = []
				is_recipe_name = False
			else:
				if len(line) > 0:
					recipes[recipe_name].append(line)
				else:
					is_recipe_name = True
	return recipes


def search_by_name(filename:str, word:str) -> list:
	recipes = read_recipe_file(filename)
	found = []

	for recipe_name, ingredient in recipes.items():
		if word.lower() in recipe_name.lower():
			found.append(recipe_name)

	return found


def search_by_time(filename:str, prep_time: int) -> list:

	recipes = read_recipe_file(filename)
	found = []

	for recipe_name, ingredients in recipes.items():
		if int(ingredients[0]) <= prep_time:
			recipe = f'{recipe_name}, preparation time {ingredients[0]} min'
			found.append(recipe)

	return found


def search_by_ingredient(filename:str, ingredient:str) -> list:

	recipes = read_recipe_file(filename)
	found = []

	for recipe_name, recipe_ingredient in recipes.items():
		if ingredient in recipe_ingredient[1:]:
			recipe = f'{recipe_name}, preparation time {recipe_ingredient[0]} min'
			found.append(recipe)
	return found

# # main
# found = search_by_name('recipes1.txt', 'cake')
# print(found)
# print()

# found_recipes = search_by_time("recipes1.txt", 20)
# for recipe in found_recipes:
#     print(recipe)
# print()

# found_recipes = search_by_ingredient("recipes1.txt", "eggs")
# for recipe in found_recipes:
#     print(recipe)