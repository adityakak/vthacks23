import pandas as pd
import requests
import googlemaps
from pathlib import Path
import os
from collections import defaultdict
import pickle

class School():
    def __init__(self, schoolName, schoolRating, schoolState):
        self.schoolName = schoolName
        self.schoolRating = schoolRating
        self.state = schoolState

    def __eq__(self, other):
        return self.schoolName == other.schoolName and self.state == other.state and self.schoolRating == other.schoolRating
    
    def __hash__(self):
        return hash((self.schoolName, self.state, self.schoolRating))

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
        self.schools = []
        for i in range(3):
            self.schools.append(School(self.data['schools/' + str(i) + '/name'], self.data['schools/' + str(i) + '/rating'], self.state))
        # self.elementarySchool = School(self.data['schools/0/name'], self.data['schools/0/rating'], self.state)
        # self.middleSchool = School(self.data['schools/1/name'], self.data['schools/1/rating'], self.state)
        # self.highSchool = School(self.data['schools/2/name'], self.data['schools/2/rating'], self.state)
class EducationAPI():
    def __init__(self, home=None):
        self.home = home
        self.authKey = self.getAuthKey()
        self.gmaps = googlemaps.Client(self.authKey)

    def setHome(self, home):
        self.home = home

    def getAuthKey(self):
        dataPath = Path(os.path.join(os.getcwd(), "education/auth.txt"))
        with open(dataPath, 'r') as authFile:
            authKey = authFile.readline()
            authKey = authKey.strip()
            return authKey

    # def getPlaceFromLatLong(self, lat, long):
    def getPlaceFromLatLong(self):
        reverse_geocode_result = self.gmaps.reverse_geocode((self.home.latitude, self.home.longitude))
        placeID = reverse_geocode_result[0]['place_id']
        return placeID
    
    def getReviewsFromPlace(self, placeID):
        reviews = self.gmaps.place(placeID, fields=['reviews', 'rating'], reviews_sort="newest")

        result = [reviews['result']['rating']]
        for reviewIndex, review in reviews['result']['reviews']:
            result.append(review['text'])
        return result # List where first value is overall rating and the rest are reviews
    
    #def findLibrariesNearLocation(self, loc):
    def findLibrariesNearLocation(self):
        libraries = self.gmaps.places_nearby(location=(self.home.latitude, self.home.longitude), type="library", radius=10000)
        
        result = []
        for library in libraries['results']:
            result.append((library['name'], library['place_id']))
        return result
    
    #def findChildCareNearLocation(self, loc):
    def findChildCareNearLocation(self):
        childCare = self.gmaps.places_nearby(location=(self.home.latitude, self.home.longitude), keyword="child care, daycare", radius=10000)
        
        result = []
        for childCare in childCare['results']:
            result.append((childCare['name'], childCare['place_id']))
        return result

if __name__ == "__main__":
    dataPath = Path(os.path.join(os.getcwd(), "houses/houseData/novaHousesSchoolsClean.csv"))
    df = pd.read_csv(dataPath)

    schoolsToHome = defaultdict(list)
    librariesToHome = defaultdict(list)
    childCareToHome = defaultdict(list)
    #houseData = defaultdict(dict)

    eduAPI = EducationAPI(None)
    for index, row in df.iterrows():
        h = Home(row)
        eduAPI.setHome(h)
        print(f"Processing {h.street} at lat {h.latitude} and long {h.longitude}")
        # placeID = eduAPI.getPlaceFromLatLong(h.latitude, h.longitude)
        placeID = eduAPI.getPlaceFromLatLong()
        for school in h.schools:
            schoolsToHome[school].append(placeID)
        for library in eduAPI.findLibrariesNearLocation():
            librariesToHome[library].append(placeID)
        for care in eduAPI.findChildCareNearLocation():
            childCareToHome[care].append(placeID)
        print(f"Finished {index} of {len(df)}")
        print()
    with open('schoolsToHome', 'wb') as file:
        pickle.dump(schoolsToHome, file)
    with open('librariesToHome', 'wb') as file:
        pickle.dump(librariesToHome, file)
    with open('childCareToHome', 'wb') as file:
        pickle.dump(childCareToHome, file)
    print()
    
    # result = eduAPI.findChildCareNearLocation((38.904960, -77.390170))
    #placedID = eduAPI.getPlaceFromLatLong(38.984830, -77.377110)
    #print()
        
    # result = eduAPI.findLibraries((38.904960, -77.390170))
    # print(result)
    # placeID = eduAPI.getPlaceFromLatLong(37.242210, -80.417152)
    # eduAPI.getReviewsFromPlace(placeID)

    #Process schools
    

