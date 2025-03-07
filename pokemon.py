import requests

base_url = "https://pokeapi.co/api/v2/"

def get_info_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"data could not be retrieved {response.status_code}")
while True:
    poke_name = input("Enter the name of the pokemon you wanna see the data: ")
    pokemon_info = get_info_pokemon(poke_name)

    if pokemon_info:
        print(f"name: {pokemon_info["name"]}")
        print(f"Id: {pokemon_info["id"]}")
        print(f"Height: {pokemon_info["height"]}")
    else:
        break