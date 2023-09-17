from flask import Flask, request, jsonify
from flask_cors import CORS
from education.educationAPI import getEducationData
from environment.environmentApi import getEnvironmentData
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
        print(request.json)
        full_address = request.json['full_address']
        half_address = request.json['half_address']
        educationData = getEducationData(full_address)
        print(f"Education Data: {educationData}")
        environmentData = getEnvironmentData(full_address)
        print(f"Environment Data: {environmentData}")

        allData = None
        with open(Path(os.path.join(os.getcwd(), "pkldata/sortedScores")), 'rb') as file:
            allData = pickle.load(file)
        allData = allData[:5]
        photosData = []
        homesLinks = []
        addy = []
        for i in allData:
            address = i[1]
            splitted = address.split(" ")
            abbreviated = splitted[0] + " " + splitted[1] + " " + splitted[2]
            print(abbreviated)
            photosData.append(getPhotoData(abbreviated))
            homesLinks.append(getHomesLink(abbreviated))
            addy.append(address)

        return jsonify({
            "education": educationData,
            "photos": photosData,
            "homeLinks": homesLinks,
            "environment": environmentData,
            "address": addy
        })

        # Handle actual request
        # call educationAPI to get data points
        # call environmentAPI to get data points
        # create method here to combine data points

        # full_address = request.json['full_address']
        # half_address = request.json['half_address']
        # educationData = getEducationData(full_address)
        # photoData = getPhotoData(half_address)
        # environmentData = getEnvironmentData(full_address)

        # dataPath = Path(os.path.join(os.getcwd(), "houses/houseData/novaHousesSchoolsClean.csv"))
        # df = pd.read_csv(dataPath)
        # results = []
        # for index, row in df.iterrows():
        #     abbreviatedAddress = row['abbreviatedAddress']
        #     city = row['address/city']
        #     state = row['address/state']
        #     zipcode = row['address/zipcode']
        #     address = f"{abbreviatedAddress}, {city}, {state} {zipcode}"
        #     eduData = getEducationData(address)
        #     envData = getEnvironmentData(address)
        #     totalScore = .5 * eduData[-1] + .5 * envData[-1]
        #     results.append((totalScore, address))
        # results.sort(reverse=True)
        # dataPath = Path(os.path.join(os.getcwd(), "pkldata/sortedScores"))
        # with open(dataPath, 'wb') as file:
        #     pickle.dump(results, file)
        
if __name__ == '__main__':
    # half_address = "908 Ashburn St"
    # full_address = "908 Ashburn St, Herndon, VA 20170"
    # getHomesLink("908 Ashburn St")
    app.run(host = "0.0.0.0", port=8080)

    # full_address = request.json['full_address']
    # half_address = request.json['half_address']
    # full_address = "908 Ashburn St, Herndon, VA 20170"
    # half_address = "908 Ashburn St"
    # educationData = getEducationData(full_address)
    # print(f"Education Data: {educationData}")
    # photoData = getPhotoData(half_address)
    # print(f"Photo Data: {photoData}")
    # environmentData = getEnvironmentData(full_address)
    # print(f"Environment Data: {environmentData}")

    # dataPath = Path(os.path.join(os.getcwd(), "houses/houseData/novaHousesSchoolsClean.csv"))
    # df = pd.read_csv(dataPath)
    # results = []
    # for index, row in df.iterrows():
    #     print(f"In progress: {index}")
    #     abbreviatedAddress = row['abbreviatedAddress']
    #     city = row['address/city']
    #     state = row['address/state']
    #     zipcode = row['address/zipcode']
    #     address = f"{abbreviatedAddress}, {city}, {state} {zipcode}"
    #     eduData = getEducationData(address)
    #     envData = getEnvironmentData(address)
    #     totalScore = .5 * eduData[-1] + .5 * envData[-1]
    #     results.append((totalScore, address))
    # results.sort(reverse=True)
    # dataPath = Path(os.path.join(os.getcwd(), "pkldata/sortedScores"))
    # with open(dataPath, 'wb') as file:
    #     pickle.dump(results, file)

