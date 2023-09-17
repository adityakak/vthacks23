from flask import Flask, request, jsonify
from flask_cors import CORS
from education.educationAPI import getEducationData
from extra.extra import getPhotoData, getHomesLink

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
        # call educationAPI to get data points
        # call environmentAPI to get data points
        # create method here to combine data points
        full_address = request.json['full_address']
        half_address = request.json['half_address']


if __name__ == '__main__':
    # half_address = "908 Ashburn St"
    # full_address = "908 Ashburn St, Herndon, VA 20170"
    # educationData = getEducationData(full_address)
    # photoData = getPhotoData(half_address)
    # print(f"Education Data: {educationData}")
    # print(f"Photo Data: {photoData}")
    getHomesLink("908 Ashburn St")
    #app.run(host = "0.0.0.0")

# 