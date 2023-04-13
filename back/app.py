from flask import Flask, after_this_request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/api/layout', methods=['POST'])
def get_data():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    data = {'message': 'Layout submitted'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='localhost', port=5000)