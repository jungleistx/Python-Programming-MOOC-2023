# tee ratkaisu tänne
# Write your solution here

import math

def get_station_data(filename:str) -> dict:
	stations = {}
	with open(filename) as file:

		for line in file:
			line = line.replace('\n', '')
			line = line.split(';')

			if line[0] == 'Longitude':
				continue
			stations[line[3]] = (float(line[0]), float(line[1]))

	return stations


def distance(stations:dict, station1:str, station2:str) -> float:
	longitude1 = float(stations[station1][0])
	longitude2 = float(stations[station2][0])
	latitude1 = float(stations[station1][1])
	latitude2 = float(stations[station2][1])

	x_km = (longitude1 - longitude2) * 55.26
	y_km = (latitude1 - latitude2) * 111.2
	distance_km = math.sqrt(x_km**2 + y_km**2)

	return distance_km


def greatest_distance(stations:dict) -> tuple:

	max_distance = 0.0
	for station1 in stations:
		for station2 in stations:
			current_distance = distance(stations, station1, station2)
			if current_distance > max_distance:
				max_distance = current_distance
				station1_name = station1
				station2_name = station2

	return station1_name, station2_name, max_distance


# # main
# stations = get_station_data('stations1.csv')
# for name, info in stations.items():
# 	print(name, info)
# print()

# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)
# print()

# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)