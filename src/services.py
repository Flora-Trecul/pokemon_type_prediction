import requests, json, fnmatch, os, csv
from pathlib import Path

def process_api_request(endpoint):
	try:
		response = requests.get(f"https://pokeapi.co/api/v2/{endpoint}")
		return response.json()
	except Exception as e:
		print(f"Error: {str(e)}")
		return None


def get_json_data(dirpath, index, species):
	filename = f"{index}.json"
	filepath = dirpath + filename

	if not Path(filepath).exists():
		data = process_api_request(f"pokemon-species/{index}") if species \
		else process_api_request(f"pokemon/{index}")

		if data:
			with open(filepath, "w") as file:
				json.dump(data, file)
			return True


def get_all_raw_data(number_pokemons, path_pokemons, path_species):
	for i in range(1, number_pokemons + 1):

		try:
			pokemon_created = get_json_data(path_pokemons, i, species=False)
			specie_created = get_json_data(path_species, i, species=True)

			if pokemon_created or specie_created:
				print(f"Pokemon n° {i} added to Pokedex")

		except Exception as e:
			print(f"Error: {str(e)}")
			continue


def count_json_files_in_dir(dirpath):
	number_files = len(fnmatch.filter(os.listdir(dirpath), "*.json"))
	return number_files


def check_pokemon_count_api():
	response = process_api_request("pokemon-species")
	number_api_pokemons = response["count"]
	return number_api_pokemons

def create_dir_if_not_exists(dirpath):
	if not os.path.exists(dirpath):
		os.makedirs(dirpath)



def complete_pokedex():
	dir_pokemons = "src/data/raw/pokemons/"
	dir_species = "src/data/raw/species/"

	number_api_pokemons = check_pokemon_count_api()

	create_dir_if_not_exists(dir_pokemons)
	create_dir_if_not_exists(dir_species)

	number_json_pokemons = count_json_files_in_dir(dir_pokemons)
	number_json_species = count_json_files_in_dir(dir_species)

	if number_api_pokemons > number_json_pokemons or number_api_pokemons > number_json_species:
		print("--- Catching missing Pokemons...")
		get_all_raw_data(number_api_pokemons, dir_pokemons, dir_species)
		create_pokedex_csv(dir_species)
	else:
		print("--- Pokedex is already complete!")



def get_pokemon_full_data(data_species, data_pokemons):
	full_pokemon_data = {
		'id': data_species['id'],
		'name_en': data_species['name'],
		'name_fr': data_species['names'][4]['name'],
		'type_1': data_pokemons['types'][0]['type']['name'],
		'type_2': data_pokemons['types'][1]['type']['name'] if len(data_pokemons['types']) > 1 else None,
		'generation': data_species['generation']['url'].split('/')[-2],
		'evolution_level': 0 if not data_species['evolves_from_species'] else 1,
		'evolves_from': data_species['evolves_from_species']['name'] if data_species['evolves_from_species'] else None,
		'is_baby': data_species['is_baby'],
		'is_legendary': data_species['is_legendary'],
		'is_mythical': data_species['is_mythical'],
		'height': data_pokemons['height'],
		'weight': data_pokemons['weight'],
		'base_experience': data_pokemons['base_experience'],
		'base_happiness': data_species['base_happiness'],
		'capture_rate': data_species['capture_rate'],
		'gender_rate': data_species['gender_rate'],
		'growth_rate': data_species['growth_rate']['name'],
		'hatch_counter': data_species['hatch_counter'],
	}


	for stat in data_pokemons['stats']:
		full_pokemon_data[f'{stat['stat']['name']}'] = stat['base_stat']
		full_pokemon_data[f'{stat['stat']['name']}_effort'] = stat['effort']
	

	return full_pokemon_data


def get_all_pokemons_full_data(dir_species):
	full_data = []
	
	for file in Path(dir_species).iterdir():
		with open(file, 'r') as f:
			data_species = json.load(f)


		file_pokemon = f.name.replace('species', 'pokemons')
		with open(file_pokemon, 'r') as f:
			data_pokemons = json.load(f)


		full_pokemon_data = get_pokemon_full_data(data_species, data_pokemons)	
		full_data.append(full_pokemon_data)
	

	return full_data


def create_pokedex_csv(dir_species):
	fieldnames = ['id', 'name_en', 'name_fr', 'type_1', 'type_2', 'generation', 'evolution_level', 'evolves_from', 'is_baby', 'is_legendary', 'is_mythical', 'height', 'weight', 'base_experience', 'base_happiness', 'capture_rate', 'gender_rate', 'growth_rate', 'hatch_counter', 'hp', 'hp_effort', 'attack', 'attack_effort', 'defense', 'defense_effort', 'special-attack', 'special-attack_effort', 'special-defense', 'special-defense_effort', 'speed', 'speed_effort']

	full_data = get_all_pokemons_full_data(dir_species)

	with open('src/data/pokedex.csv', mode='w', newline='', encoding='utf-8') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(full_data)
