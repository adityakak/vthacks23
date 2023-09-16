from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ratings', methods=['POST', 'OPTIONS'])
def ratings():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'status': 'success'})
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    else:
        # Handle actual request
        return jsonify({'status': 'success'})