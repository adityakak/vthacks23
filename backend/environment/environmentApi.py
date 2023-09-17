from pathlib import Path
import os
import sys
import requests
import json
import pandas as pd
# import credentials
import googlemaps
import pickle
from collections import defaultdict

class Home():
    def __init__(self, dfRow):
        self.data = dfRow
        self.homeStatus = self.data['homeStatus']
        self.city = self.data['address/city']
        self.street = self.data['address/streetAddress']
        self.state = self.data['address/state']
        self.zipCode = self.data['address/zipcode']
        self.latitude = self.data['latitude']
        self.longitude = self.data['longitude']
        self.aqi_average = None
        self.highest_energy_output = None
        self.placeID = None
        self.num_chargers = None
    
    def setPlaceID(self, place_id: str):
        self.placeID = place_id
    
    def setAqiAverage(self, aqi_average: int):
        self.aqi_average = aqi_average
    
    def setHighestEnergy(self, highest_energy: int):
        self.highest_energy_output = highest_energy
    
    def setNumChargers(self, num_chargers):
        self.num_chargers = num_chargers


class EnvironmentApi:
    def __init__(self, home=None, url=None) -> None:
        self.home = home
        self.api_key = getGoogleAuthKey()
        self.header = { 'Content-Type': 'application/json'}
        self.aqi_request_data_history = {
            "hours": 168,
            "pageSize": 168,
            "pageToken":"",
            "location": {
                "latitude": None,
                "longitude": None
            }
        }
        self.aqi_url_history = f'https://airquality.googleapis.com/v1/history:lookup?key={self.api_key}'
        self.solar_url = url
        self.gmaps = googlemaps.Client(getGoogleAuthKey())

    def setHome(self, home: Home):
        self.home = home
        self.solar_url = f'https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={self.home.latitude}&location.longitude={self.home.longitude}&requiredQuality=HIGH&key={self.api_key}'
        self.getPlaceID()    
    
    def getPlaceID(self):
        reverse_geocode_result = self.gmaps.reverse_geocode((self.home.latitude, self.home.longitude))
        self.home.setPlaceID(reverse_geocode_result[0]['place_id']) 

    def load_air_quality(self):
        self.configure_request_data()
        data = json.dumps(self.aqi_request_data_history)
        response = requests.post(self.aqi_url_history, data=data, headers=self.header)
        response = response.json()["hoursInfo"]
        aqi_sum = 0
        for i in range(0, len(response)):
            indexes = response[i]['indexes']
            aqi_sum += indexes[0]['aqi']
        self.home.setAqiAverage(aqi_average=aqi_sum/len(response))

    def configure_request_data(self):
        self.aqi_request_data_history['location']['latitude'] = self.home.latitude
        self.aqi_request_data_history['location']['longitude'] = self.home.longitude

    def load_solar_quality(self):
        response = requests.get(self.solar_url, headers=self.header)
        try:
            response = response.json()['solarPotential']['solarPanelConfigs']
            highest_output_config = response[len(response)-1]
            self.home.setHighestEnergy(highest_output_config['yearlyEnergyDcKwh'])
        except KeyError:
            self.home.setHighestEnergy(-1)

    def findNearbyChargers(self):
        chargers = self.gmaps.places_nearby(location=(self.home.latitude, self.home.longitude), type="electric car charging stations", radius=3400)
        for i in chargers['results']:
            print(i['name']+", "+i['place_id'])
        self.home.setNumChargers(len(chargers['results']))

def getGoogleAuthKey(self):
        dataPath = Path(os.path.join(os.getcwd(), "environment/googleAuth.txt"))
        with open(dataPath, 'r') as authFile:
            authKey = authFile.readline()
            authKey = authKey.strip()
            return authKey


def getEnvironmentData(address: str):
    gmaps = googlemaps.Client(getGoogleAuthKey())
    dataPath = Path(os.path.join(os.getcwd(), 'envData/envData'))
    with open(dataPath, 'rb') as file:
        data = pickle.load(file=file)
    geocode_result = gmaps.geocode(address)
    place_id = geocode_result[0]['place_id']
    max_aqi = 0
    max_solar_potential = 0
    max_num_chargers = 0
    for key in data.keys():
        if data[key]['aqi'] > max_aqi:
            max_aqi = data[key]['aqi']
        if data[key]['solar_output'] > max_solar_potential:
            max_solar_potential = data[key]['solar_output']
        if data[key]['num_chargers'] > max_num_chargers:
            max_num_chargers = data[key]['num_chargers']
    house_aqi_score = 1-(data[place_id]['aqi']/max_aqi)
    house_solar_score = data[place_id]['solar_output']/max_solar_potential
    house_chargers_score = 1
    environmentScore = 0.3*house_aqi_score+0.5*house_solar_score+0.1*house_chargers_score
    return [house_aqi_score, house_solar_score, house_chargers_score, environmentScore]



if __name__ == '__main__':
    print(getEnvironmentData("908 Ashburn St, Herndon, VA 20170"))
    #relative_path = "houses/houseData/novaHousesSchoolsClean.csv"
    #dataPath = Path(os.path.join(os.getcwd(), relative_path))
    #envApi = EnvironmentApi()
    #df = pd.read_csv(dataPath)
    #environmentalDict = defaultdict(dict)
    #for i in range(0, len(df)):
    #    home = Home(df.iloc[i])
    #    envApi.setHome(home=home)
    #    envApi.load_air_quality()
    #    envApi.load_solar_quality()
    #    envApi.findNearbyChargers()
    #    environmentalDict[home.placeID] = {'aqi': home.aqi_average, 'solar_output': home.highest_energy_output, 'num_chargers': home.num_chargers}
    #    print(home.placeID+":"+str(environmentalDict[home.placeID]))
    #writePath = Path(os.path.join(os.getcwd(), "envData/envData"))
    #with open(writePath, 'wb') as file:
    #    pickle.dump(environmentalDict, file)
    
    



