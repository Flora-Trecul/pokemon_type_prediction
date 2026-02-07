import requests
import csv
from pathlib import Path

def get_data(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			data = response.json()
			return data
		else:
			print('Error:', response.status_code)
			return
	except requests.exceptions.RequestException as e:
		print('Error:', e)
		return


def get_detailed_data(url):
	print('We\'re cathcing all 1025 Pokemons, it might take a few minutes.')
	detailed_data = []

	for i in range(1025):
		print('--- Catching Pokemon n°', i + 1)
		endpoint_url = f'{url}/{i + 1}'
		details = get_data(endpoint_url)

		if details:
			full_data = {
				'pokedex_id': details['id'],
				'name': details['name'],
				'type_1': details['types'][0]['type']['name'],
				'type_2': details['types'][1]['type']['name'] if len(details['types']) > 1 else None,
				'hp': details['stats'][0]['base_stat'],
				'attack': details['stats'][1]['base_stat'],
				'defense': details['stats'][2]['base_stat'],
				'special_attack': details['stats'][3]['base_stat'],
				'special_defense': details['stats'][4]['base_stat'],
				'speed': details['stats'][5]['base_stat']
			}

			detailed_data.append(full_data)

		else:
			pass
		
	return detailed_data

def complete_pokedex():
	if not Path('./src/pokedex.csv').exists():
		print('File not found')
		base_url = 'https://pokeapi.co/api/v2/pokemon'
		pokemons_data = get_detailed_data(base_url)

		if pokemons_data:
			print('Number of Pokemons caught:', len(pokemons_data))

			csv_filename = 'pokedex.csv'
			fieldnames = ['pokedex_id', 'name', 'type_1', 'type_2', 'hp', 
						'attack', 'defense', 'special_attack', 'special_defense', 'speed']

			with open(csv_filename, mode='w', newline='') as file:
				writer = csv.DictWriter(file, fieldnames=fieldnames)
				writer.writeheader()
				writer.writerows(pokemons_data)
		else:
			print('Sorry, it seems that we couldn\'t catch any Pokemon...')
	else:
		print('Pokedex is already complete')