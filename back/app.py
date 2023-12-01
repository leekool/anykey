import glob
import os
import requests
import json
from flask import Flask, after_this_request, jsonify, request
from flask_cors import CORS

from parse_keys import parse_map
from generate_svg import get_keymap_svg
from generate_flat_svg import get_flat_keymap_svg

app = Flask(__name__)
CORS(app)

API_URL = os.environ.get('ANYKEY_URL', 'localhost')
CERT_PATH = os.environ.get('CERT_PATH')
KEY_PATH = os.environ.get('KEY_PATH')


# Gets the SVG based on chosen keyboard and uploaded map
@app.route('/api/layout', methods=['POST'])
def get_data():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    if 'file' not in request.files:
        return 'No file found'

    if 'keyboardName' not in request.form:
        return 'No map found'

    if 'mergeLayers' not in request.form:
        return 'No Merge Layer found'

    fileData = request.files['file']
    keyboardName = request.form['keyboardName']
    mergeLayers = request.form['mergeLayers']
    fullLayout = parse_map(fileData)

    if (mergeLayers == 'true'):
        svg_string = get_flat_keymap_svg(keyboardName, fullLayout)
    else:
        svg_string = get_keymap_svg(keyboardName, fullLayout)

    return jsonify({'message': svg_string})

@app.route('/api/keyboards', methods=['GET'])
def get_keyboards():
    fileNames = []

    print('boutta geddit')
    response = requests.get(f"https://api.qmk.fm/v1/keyboards")
    keyboardList = json.loads(response.content)

    print(keyboardList)

    return keyboardList


if __name__ == "__main__":
    if API_URL == 'localhost':
        app.run(debug=True, host=API_URL, port=5000)
    else:
        app.run(ssl_context=(CERT_PATH, KEY_PATH), host=API_URL, port=5000)
