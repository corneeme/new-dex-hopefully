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
    try:
        limit = request.args.get('limit', 1025, type=int)
        # Cap the limit to a reasonable value to avoid hanging
        limit = min(limit, 1025)
        response = requests.get(f'{POKEAPI_BASE}/pokemon?limit={limit}', timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.Timeout:
        return jsonify({'error': 'Request timeout'}), 504
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/pokemon/<pokemon_id>')
def get_pokemon_details(pokemon_id):
    try:
        response = requests.get(f'{POKEAPI_BASE}/pokemon/{pokemon_id}', timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.Timeout:
        return jsonify({'error': 'Request timeout'}), 504
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/pokemon-species/<species_id>')
def get_pokemon_species(species_id):
    try:
        response = requests.get(f'{POKEAPI_BASE}/pokemon-species/{species_id}', timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.Timeout:
        return jsonify({'error': 'Request timeout'}), 504
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/evolution-chain/<chain_id>')
def get_evolution_chain(chain_id):
    try:
        response = requests.get(f'{POKEAPI_BASE}/evolution-chain/{chain_id}', timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.Timeout:
        return jsonify({'error': 'Request timeout'}), 504
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/move')
def get_moves():
    try:
        limit = request.args.get('limit', 100, type=int)
        limit = min(limit, 1000)
        response = requests.get(f'{POKEAPI_BASE}/move?limit={limit}', timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.Timeout:
        return jsonify({'error': 'Request timeout'}), 504
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/move/<move_id>')
def get_move_details(move_id):
    try:
        response = requests.get(f'{POKEAPI_BASE}/move/{move_id}', timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.Timeout:
        return jsonify({'error': 'Request timeout'}), 504
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ability')
def get_abilities():
    try:
        limit = request.args.get('limit', 100, type=int)
        limit = min(limit, 1000)
        response = requests.get(f'{POKEAPI_BASE}/ability?limit={limit}', timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.Timeout:
        return jsonify({'error': 'Request timeout'}), 504
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ability/<ability_id>')
def get_ability_details(ability_id):
    try:
        response = requests.get(f'{POKEAPI_BASE}/ability/{ability_id}', timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.Timeout:
        return jsonify({'error': 'Request timeout'}), 504
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
