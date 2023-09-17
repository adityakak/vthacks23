from flask import Flask, request, jsonify
from flask_cors import CORS
from education.educationAPI import getEducationData
from environment.environmentAPI import getEnvironmentData
from extra.extra import getPhotoData, getHomesLink
import pandas as pd
from pathlib import Path
import os
import pickle

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
        educationData = getEducationData(full_address)
        photoData = getPhotoData(half_address)
        environmentData = getEnvironmentData(full_address)

        dataPath = Path(os.path.join(os.getcwd(), "houses/houseData/novaHousesSchoolsClean.csv"))
        df = pd.read_csv(dataPath)
        results = []
        for index, row in df.iterrows():
            abbreviatedAddress = row['abbreviatedAddress']
            city = row['address/city']
            state = row['address/state']
            zipcode = row['address/zipcode']
            address = f"{abbreviatedAddress}, {city}, {state} {zipcode}"
            eduData = getEducationData(address)
            envData = getEnvironmentData(address)
            totalScore = .5 * eduData['totalScore'] + .5 * envData['totalScore']
            results.append((totalScore, address))
        results.sort(reverse=True)
        dataPath = Path(os.path.join(os.getcwd(), "pkldata/sortedScores"))
        with open(dataPath, 'wb') as file:
            pickle.dump(results, file)


        # print(f"Education Data: {educationData}")
        # print(f"Photo Data: {photoData}")


if __name__ == '__main__':
    # half_address = "908 Ashburn St"
    # full_address = "908 Ashburn St, Herndon, VA 20170"
    getHomesLink("908 Ashburn St")
    #app.run(host = "0.0.0.0")

# 