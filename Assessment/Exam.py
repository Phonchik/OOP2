import requests as requests


class BasePokemon:
    def __init__(self, name):
        self.name = name


class Pokemon(BasePokemon):
    def __init__(self, id, height, weight, name):
        super().__init__(name)
        self.id = id
        self.height = height
        self.weight = weight

#class PokeAPI
#    def get_pokemon:
#
#    def get_all:
 #       get_full = False





poke = requests.get("https://pokeapi.co/api/v2/pokemon/ditto").json()
poke[]

