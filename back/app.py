import glob
import os
from flask import Flask, after_this_request, jsonify, request
from flask_cors import CORS, cross_origin

from parse_keys import parse_map
from generate_flat_svg import get_keymap_svg

app = Flask(__name__)
CORS(app)

# Gets the SVG based on chosen keyboard and uploaded map
@app.route('/api/layout', methods=['POST'])
def get_data():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    if 'file' not in request.files:
        return 'No file found'
    
    if 'mapPath' not in request.form:
        return 'No map found'
    
    fileData = request.files['file']
    mapPath = request.form['mapPath']
    fullLayout = parse_map(fileData)

    svg_string = get_keymap_svg(mapPath, fullLayout)

    return jsonify({'message': svg_string})

# Gets the List<String, String> of keyboard we have
@app.route('/api/keyboards', methods=['GET'])
def get_keyboards():
    fileNames = []
    for fileName_absolute in glob.glob('./keymap_layouts/**/*.json',recursive=True):
        # filename, filename path
        fileNames.append({'name': os.path.basename(fileName_absolute).replace('.json', ''), 'path': fileName_absolute})

    fileNames.sort(key=lambda x: x['name'])
    return fileNames

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)