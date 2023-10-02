# Write your solution here

import json

def main():
	players = load_players()
	selection_loop(players)


def print_commands():
	print('''commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals''')


def load_players() -> list:
	filename = ''
	while len(filename) < 1:
		filename = input('file name: ')

	try:
		with open(filename) as file:
			data = file.read()
			players = json.loads(data)
			print(f'read the data of {len(players)} players\n')
			return players
	except:
		print('Error reading file!')
		exit()


def search_players(players:list):
	name = ''
	while len(name) < 1:
		name = input('name: ')
	name = name.lower()

	for player in players:
		if player['name'].lower() == name:
			print()
			print_player(player)
			return


def print_player(player:dict):
	print(f"{player['name']:21}{player['team']}", end='')
	print(f"{player['goals']:>4} + {player['assists']:>2} = {player['goals'] + player['assists']:>3}")


def print_teams(players:list):
	teams = set(player['team'] for player in players)
	for team in sorted(teams):
		print(team)


def print_nationalities(players:list):
	countries = set(player['nationality'] for player in players)
	for country in sorted(countries):
		print(country)


def print_team_players(players:list):
	team = ''
	while len(team) == 0:
		team = input('team: ')
	team = team.upper()

	team_players = [player for player in players if player['team'] == team]
	team_players.sort(key=lambda x: (x['goals'] + x['assists'], x['goals']), reverse=True)

	if team_players:
		print()
		for player in team_players:
			print_player(player)


def print_country_players(players:list):
	country = ''
	while len(country) == 0:
		country = input('country: ')
	country = country.upper()

	country_players = [player for player in players if player['nationality'] == country]
	country_players.sort(key=lambda x: (x['goals'] + x['assists'], x['goals']), reverse=True)

	if country_players:
		print()
		for player in country_players:
			print_player(player)


def get_amount() -> int:
	while True:
		try:
			amount = int(input('how many: '))
			return amount
		except:
			pass


def most_points(players:list):
	amount = get_amount()
	all_players = sorted(players, key=lambda x: (x['goals'] + x['assists'], x['goals']), reverse=True)
	if all_players:
		print()
		for i in range(amount):
			print_player(all_players[i])


def most_goals(players:list):
	amount = get_amount()

	all_players = sorted(players, key=lambda x: (x['goals'], x['games'] * -1), reverse=True)
	if all_players:
		print()
		for i in range(amount):
			print_player(all_players[i])


def selection_loop(players:list):
	print_commands()
	while True:
		print()
		selection = input('command: ')

		if selection == '0':
			return
		elif selection == '1':
			search_players(players)
		elif selection == '2':
			print_teams(players)
		elif selection == '3':
			print_nationalities(players)
		elif selection == '4':
			print_team_players(players)
		elif selection == '5':
			print_country_players(players)
		elif selection == '6':
			most_points(players)
		elif selection == '7':
			most_goals(players)


main()
