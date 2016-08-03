#!/usr/bin/env python
import requests
poke = "http://pokeapi.co/api/v2/"
pokemon = poke + "pokemon/"

def get_info():
    pokename = raw_input("Which Pokemon would you like to see?: ")
    pokename = pokename.lower()
    pokemon_details = requests.get(pokemon + pokename)
    pokemon_json = pokemon_details.json()
    name = pokemon_json['name']
    number = pokemon_json['id']
    poke_type = pokemon_json['types'][0]['type']['name']
    print name + " is number " + str(number)
    print name + "'s type is " + poke_type

def compare_type(poke1, poke2):
    poke1 = poke1.lower()
    poke2 = poke2.lower()
    poke1_details = requests.get(pokemon + poke1 + "/")
    poke1_json = poke1_details.json()
    type1_info = poke1_json['types'][0]['type']
    type1 = type1_info['name']
    type1_json = (requests.get(type1_info['url'])).json()
    type1_weakness_list = type1_json['damage_relations']['double_damage_from']
    type1_weaknesses = []
    #for weakness1 in type1_weakness_list:
     #   type1_weakness_list.append(weakness1['name'])
    poke2_details = requests.get(pokemon + poke2 + "/")
    poke2_json = poke2_details.json()
    type2_info = poke2_json['types'][0]['type']
    type2 = type2_info['name']
    type2_json = (requests.get(type2_info['url'])).json()
    type2_weakness_list = type2_json['damage_relations']['double_damage_from']
    type2_weaknesses = []
    for weakness2 in type2_weakness_list:
        type2_weaknesses.append(weakness2['name'])
    print "You're comparing " + poke1 + " and " + poke2 + "."

    if type1 in type2_weaknesses:
        print poke1 + " is stronger."
    else:
        print poke1 + " is not stronger."



compare_type("Pikachu", "Geodude")