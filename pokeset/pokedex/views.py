from urllib import response
from django.shortcuts import render
import requests
import json


# Create your views here.
def get_main(req):
    return render(req, 'main.html')

def get_dashboard(req):
    context = {"pokemon_data": static_pokemon}
    print(context)
    set_images(context)
    return render(req, 'dashboard.html', context=context)

def get_detailed_view(req, id):
    print(req.path)
    context = {"pokemon_data": static_pokemon[0:1]}
    set_images(context)
    context = {"pokemon_data": context["pokemon_data"][0]}
    return render(req, 'detailed_view.html', context)

def get_edit_pokemon(req, id):
    print(req.path)
    context = {"pokemon_data": static_pokemon[0:1]}
    set_images(context)
    context = {"pokemon_data": context["pokemon_data"][0]}
    return render(req, 'edit_pokemon.html', context)



# Retrieves images of pokemon from pokeapi based on its name
def set_images(context):
    params = {"format": "json"}
    # For each pokemon in array
    for pokemon in context["pokemon_data"]:
        print("Looking for " + pokemon["name"].lower())
        # Query API for given pokemon and parse JSON
        try: 
            response = requests.get("https://pokeapi.co/api/v2/pokemon/" +pokemon["name"].lower(), params=params)
            print("Found it: " + response.json()["sprites"]["front_default"])
            pokemon["img"] = response.json()["sprites"]["front_default"]
        except:
            return


# To be deleted, using to test front-end
static_pokemon = [
    {   
        "id":"123",
        "name": "Charmander",
        "type1": "Fire",
        "type2": None,
        "location": "Pallet Town",
        "abilities": [
        {
            "name": "Growl",
            "type": "Normal"
        }, 
        {
            "name": "Ember",
            "type": "Fire"
        }],
        "effective": ["Grass"],
        "weakness": ["Rock", "Water"],
        "img": None
    },
    {   
        "id":"111",
        "name": "Pikachu",
        "type1": "Electric",
        "type2": None,
        "location": "Pallet Town",
        "abilities": [{
            "name": "Static",
            "type": "Normal"
        }],
        "effective": ["Flying"],
        "weakness": ["Ground", "Water"],
        "img": None
    },
    {   
        "id":"114",
        "name": "Charizard",
        "type1": "Fire",
        "type2": None,
        "location": "Pallet Town, Route 404",
        "abilities": [
        {
            "name": "Growl",
            "type": "Normal"
        }, 
        {
            "name": "Ember",
            "type": "Fire"
        }],
        "effective": ["Grass"],
        "weakness": ["Rock", "Water"],
        "img": None
    }          
]