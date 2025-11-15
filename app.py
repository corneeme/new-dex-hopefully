from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_folder='.')
CORS(app)

POKEAPI_BASE = 'https://pokeapi.co/api/v2'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/pokemon')
def get_pokemon_list():
    limit = request.args.get('limit', 1025)
    try:
        response = requests.get(f'{POKEAPI_BASE}/pokemon?limit={limit}')
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/pokemon/<pokemon_id>')
def get_pokemon_details(pokemon_id):
    try:
        response = requests.get(f'{POKEAPI_BASE}/pokemon/{pokemon_id}')
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/pokemon-species/<species_id>')
def get_pokemon_species(species_id):
    try:
        response = requests.get(f'{POKEAPI_BASE}/pokemon-species/{species_id}')
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/evolution-chain/<chain_id>')
def get_evolution_chain(chain_id):
    try:
        response = requests.get(f'{POKEAPI_BASE}/evolution-chain/{chain_id}')
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/move')
def get_moves():
    limit = request.args.get('limit', 100)
    try:
        response = requests.get(f'{POKEAPI_BASE}/move?limit={limit}')
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/move/<move_id>')
def get_move_details(move_id):
    try:
        response = requests.get(f'{POKEAPI_BASE}/move/{move_id}')
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ability')
def get_abilities():
    limit = request.args.get('limit', 100)
    try:
        response = requests.get(f'{POKEAPI_BASE}/ability?limit={limit}')
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ability/<ability_id>')
def get_ability_details(ability_id):
    try:
        response = requests.get(f'{POKEAPI_BASE}/ability/{ability_id}')
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
