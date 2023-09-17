import pandas as pd
import requests
import googlemaps
from pathlib import Path
import os
from collections import defaultdict
import pickle
from pysentimiento import create_analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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
        self.googleAuthKey = self.getGoogleAuthKey()
        self.gmaps = googlemaps.Client(self.googleAuthKey)
        self.mongoAuthKey = self.getMongoAuthKey()
        self.mongo = f'mongodb+srv://adityakak:{self.mongoAuthKey}@vthacksdata.lp1aqo8.mongodb.net/?retryWrites=true&w=majority'
        self.sia = SentimentIntensityAnalyzer()

    def setHome(self, home):
        self.home = home

    def getGoogleAuthKey(self):
        dataPath = Path(os.path.join(os.getcwd(), "education/googleAuth.txt"))
        with open(dataPath, 'r') as authFile:
            authKey = authFile.readline()
            authKey = authKey.strip()
            return authKey
        
    def getMongoAuthKey(self):
        dataPath = Path(os.path.join(os.getcwd(), "education/mongoAuth.txt"))
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

        if len(reviews['result']) == 0:
            return None
        result = [reviews['result']['rating']]
        for review in reviews['result']['reviews']:
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
    
    def findSchoolsNearLocationWithName(self):
        result = []
        for school in self.home.schools:
            s = self.gmaps.places_nearby(location=(self.home.latitude, self.home.longitude), keyword=school.schoolName, radius=10000)
            if s['status'] != 'ZERO_RESULTS':
                result.append((s['results'][0]['name'], s['results'][0]['place_id']))
        return result
        # Return a list of school place ids

    def findSentimentRatingScore(self, dataToHome):
        dataToReviews = defaultdict(list)
        for dataName, dataPlaceID in dataToHome:
            print(f"Processing {dataName}")
            reviews = eduAPI.getReviewsFromPlace(dataPlaceID)
            if reviews is None:
                continue
            dataToReviews[(dataName, dataPlaceID)].append(reviews[0])
            totalSentimentScore = [0 for i in range(3)]
            for review in reviews[1:]:
                sentimentScore = self.sia.polarity_scores(review)
                totalSentimentScore[0] += sentimentScore['neg']
                totalSentimentScore[1] += sentimentScore['neu']
                totalSentimentScore[2] += sentimentScore['pos']
                print(totalSentimentScore)
            dataToReviews[(dataName, dataPlaceID)].append(sum(totalSentimentScore) / len(totalSentimentScore))
            print()
            print(f"Data To Reviews Dict: {dataToReviews}")
            print(f"Finished {dataName}")
        return dataToReviews

if __name__ == "__main__":
    # dataPath = Path(os.path.join(os.getcwd(), "houses/houseData/novaHousesSchoolsClean.csv"))
    # df = pd.read_csv(dataPath)

    # schoolsToHome = defaultdict(list)
    # librariesToHome = defaultdict(list)
    # childCareToHome = defaultdict(list)

    # eduAPI = EducationAPI(None)
    # for index, row in df.iterrows():
    #     h = Home(row)
    #     eduAPI.setHome(h)
    #     print(f"Processing {h.street} at lat {h.latitude} and long {h.longitude}")
    #     placeID = eduAPI.getPlaceFromLatLong()
    #     # for school in h.schools:
    #     #     schoolsToHome[school].append(placeID)
    #     for school in eduAPI.findSchoolsNearLocationWithName():
    #         schoolsToHome[school].append(placeID)
    #     for library in eduAPI.findLibrariesNearLocation():
    #         librariesToHome[library].append(placeID)
    #     for care in eduAPI.findChildCareNearLocation():
    #         childCareToHome[care].append(placeID)
    #     print(f"Finished {index} of {len(df)}")
    #     print()
    # with open('schoolsToHome', 'wb') as file:
    #     pickle.dump(schoolsToHome, file)
    # with open('librariesToHome', 'wb') as file:
    #     pickle.dump(librariesToHome, file)
    # with open('childCareToHome', 'wb') as file:
    #     pickle.dump(childCareToHome, file)

    print()
    eduAPI = EducationAPI(None)
    schoolsToHome = None
    librariesToHome = None
    childCareToHome = None
    with open('childCareToHome', 'rb') as file:
        childCareToHome = pickle.load(file)
    # with open('librariesToHome', 'rb') as file:
    #     librariesToHome = pickle.load(file)
    with open('schoolsToHome', 'rb') as file:
        schoolsToHome = pickle.load(file)

    # Rating, Sentiment Score
    #librariesToReviews = eduAPI.findSentimentRatingScore(librariesToHome)
    schoolsToReviews = eduAPI.findSentimentRatingScore(schoolsToHome)
    childCareToReviews = eduAPI.findSentimentRatingScore(childCareToHome)
    with open('schoolsToReviews', 'wb') as file:
        pickle.dump(schoolsToReviews, file)
    # with open('librariesToReviews', 'wb') as file:
    #     pickle.dump(librariesToReviews, file)
    with open('childCareToReviews', 'wb') as file:
        pickle.dump(childCareToReviews, file)
    print()

    # analyzer = create_analyzer(task="sentiment", lang="en")
    

    # for libraryName, libraryPlaceID in dataToHome:
    #     print(f"Processing {libraryName}")
    #     reviews = eduAPI.getReviewsFromPlace(libraryPlaceID)
    #     dataToReviews[(libraryName, libraryPlaceID)].append(reviews[0])
    #     totalSentimentScore = [0 for i in range(3)]
    #     for review in reviews[1:]:
    #         sentimentScore = sia.polarity_scores(review)
    #         totalSentimentScore[0] += totalSentimentScore['neg']
    #         totalSentimentScore[1] += totalSentimentScore['neu']
    #         totalSentimentScore[2] += totalSentimentScore['pos']
    #         print(totalSentimentScore)
    #     dataToReviews[(libraryName, libraryPlaceID)].append(sum(totalSentimentScore) / len(totalSentimentScore))
    #     print(f"Finished {libraryName}")
    #     print()
    
    

    

