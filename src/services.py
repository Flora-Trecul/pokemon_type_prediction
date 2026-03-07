import requests, json, fnmatch, os
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
	number_api_pokemons = check_pokemon_count_api()

	path_pokemons = "src/data/raw/pokemons/"
	path_species = "src/data/raw/species/"
	create_dir_if_not_exists(path_pokemons)
	create_dir_if_not_exists(path_species)

	number_json_pokemons = count_json_files_in_dir(path_pokemons)
	number_json_species = count_json_files_in_dir(path_species)

	if number_api_pokemons > number_json_pokemons or number_api_pokemons > number_json_species:
		print("--- Catching missing Pokemons...")
		get_all_raw_data(number_api_pokemons, path_pokemons, path_species)
	else:
		print("--- Pokedex is already complete!")
