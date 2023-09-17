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
    
    def getPlaceFromAddress(self, address):
        geocode_result = self.gmaps.geocode(address)
        placeID = geocode_result[0]['place_id']
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
            reviews = self.getReviewsFromPlace(dataPlaceID)
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
    
def dumpData(fileName, data):
    dataPath = Path(os.path.join(os.getcwd(), f"pkldata/{fileName}"))
    with open(dataPath, 'wb') as file:
        pickle.dump(data, file)

def loadData(fileName):
    dataPath = Path(os.path.join(os.getcwd(), f"pkldata/{fileName}"))
    with open(dataPath, 'rb') as file:
        data = pickle.load(file)
    return data

def readData(fileName):
    dataPath = Path(os.path.join(os.getcwd(), fileName))
    df = pd.read_csv(dataPath)

    schoolsToHome = defaultdict(list)
    librariesToHome = defaultdict(list)
    childCareToHome = defaultdict(list)

    eduAPI = EducationAPI(None)

    for index, row in df.iterrows():
        h = Home(row)
        eduAPI.setHome(h)
        print(f"Processing {h.street} at lat {h.latitude} and long {h.longitude}")
        placeID = eduAPI.getPlaceFromLatLong()
        for school in eduAPI.findSchoolsNearLocationWithName():
            schoolsToHome[school].append(placeID)
        for library in eduAPI.findLibrariesNearLocation():
            librariesToHome[library].append(placeID)
        for care in eduAPI.findChildCareNearLocation():
            childCareToHome[care].append(placeID)
        print(f"Finished {index} of {len(df)}")
        print()
    dumpData('schoolsToHome', schoolsToHome)
    dumpData('librariesToHome', librariesToHome)
    dumpData('childCareToHome', childCareToHome)
    # with open('schoolsToHome', 'wb') as file:
    #     pickle.dump(schoolsToHome, file)
    # with open('librariesToHome', 'wb') as file:
    #     pickle.dump(librariesToHome, file)
    # with open('childCareToHome', 'wb') as file:
    #     pickle.dump(childCareToHome, file)

def scoreData():
    eduAPI = EducationAPI(None)
    schoolsToHome = None
    librariesToHome = None
    childCareToHome = None
    # with open('childCareToHome', 'rb') as file:
    #     childCareToHome = pickle.load(file)
    # with open('librariesToHome', 'rb') as file:
    #     librariesToHome = pickle.load(file)
    # with open('schoolsToHome', 'rb') as file:
    #     schoolsToHome = pickle.load(file)
    schoolsToHome = loadData('schoolsToHome')
    librariesToHome = loadData('librariesToHome')
    childCareToHome = loadData('childCareToHome')

    # Rating, Sentiment Score
    librariesToReviews = eduAPI.findSentimentRatingScore(librariesToHome)
    schoolsToReviews = eduAPI.findSentimentRatingScore(schoolsToHome)
    childCareToReviews = eduAPI.findSentimentRatingScore(childCareToHome)
    # with open('schoolsToReviews', 'wb') as file:
    #     pickle.dump(schoolsToReviews, file)
    # with open('librariesToReviews', 'wb') as file:
    #     pickle.dump(librariesToReviews, file)
    # with open('childCareToReviews', 'wb') as file:
    #     pickle.dump(childCareToReviews, file)
    # print()
    schoolsToReviews = dumpData('schoolsToReviews', schoolsToReviews)
    librariesToReviews = dumpData('librariesToReviews', librariesToReviews)
    childCareToReviews = dumpData('childCareToReviews', childCareToReviews)

def condenseData(data, settify):
    if settify:
        condensedData = defaultdict(set)
    else:
        condensedData = defaultdict(list)
    for key, value in data.items():
        name, placeID = key[0], key[1]
        for val in value:
            if settify:
                condensedData[placeID].add(val)
            else:
                condensedData[placeID].append(val)
    return condensedData

def getEducationData(address):
    eduAPI = EducationAPI(None)
    placeID = eduAPI.getPlaceFromAddress(address)
    #placeID = 'ChIJf1KNmBSzt4kRxpjfyRXLaKw'


    # schoolsToHome = loadData('schoolsToHome')
    # librariesToHome = loadData('librariesToHome')
    # childCareToHome = loadData('childCareToHome')  

    # schoolsToReviews = loadData('schoolsToReviews')
    # librariesToReviews = loadData('librariesToReviews')
    # childCareToReviews = loadData('childCareToReviews')  

    # schoolsToHomeCondensed = condenseData(schoolsToHome, True)
    # librariesToHomeCondensed = condenseData(librariesToHome, True)
    # childCareToHomeCondensed = condenseData(childCareToHome, True)

    # schoolsToReviewsCondensed = condenseData(schoolsToReviews, False)
    # librariesToReviewsCondensed = condenseData(librariesToReviews, False)
    # childCareToReviewsCondensed = condenseData(childCareToReviews, False)

    # print()

    # dumpData('schoolsToHomeCondensed', schoolsToHomeCondensed)
    # dumpData('librariesToHomeCondensed', librariesToHomeCondensed)
    # dumpData('childCareToHomeCondensed', childCareToHomeCondensed)

    # dumpData('schoolsToReviewsCondensed', schoolsToReviewsCondensed)
    # dumpData('librariesToReviewsCondensed', librariesToReviewsCondensed)
    # dumpData('childCareToReviewsCondensed', childCareToReviewsCondensed)

    schoolsToHomeCondensed = loadData('schoolsToHomeCondensed')
    librariesToHomeCondensed = loadData('librariesToHomeCondensed')
    childCareToHomeCondensed = loadData('childCareToHomeCondensed')

    schoolsToReviewsCondensed = loadData('schoolsToReviewsCondensed')
    librariesToReviewsCondensed = loadData('librariesToReviewsCondensed')
    childCareToReviewsCondensed = loadData('childCareToReviewsCondensed')

    # toRemove = []
    # for key in schoolsToHomeCondensed:
    #     if key not in schoolsToReviewsCondensed:
    #         toRemove.append(key)
    # for key in toRemove:
    #     del schoolsToHomeCondensed[key]

    # toRemove = []
    # for key in librariesToHomeCondensed:
    #     if key not in librariesToReviewsCondensed:
    #         toRemove.append(key)
    # for key in toRemove:
    #     del librariesToHomeCondensed[key]

    # toRemove = []
    # for key in childCareToHomeCondensed:
    #     if key not in childCareToReviewsCondensed:
    #         toRemove.append(key)
    # for key in toRemove:
    #     del childCareToHomeCondensed[key]
    
    # print()

    childCare = []
    libraries = []
    schools = []

    for care, houses in childCareToHomeCondensed.items():
        if placeID in houses:
            childCare.append(care)
    for library, houses in librariesToHomeCondensed.items():
        if placeID in houses:
            libraries.append(library)
    for school, houses in schoolsToHomeCondensed.items():
        if placeID in houses:
            schools.append(school)
    
    bestChildCareScoreOverall = bestChildCareOverall = 0
    bestLibraryScoreOverall = bestLibraryOverall = 0
    bestSchoolScoreOverall = bestSchoolOverall = 0

    GOOGLE_SCORE = 0
    SENTIMENT_SCORE = 1
    for care, ratings in childCareToReviewsCondensed.items():
        score = 0.75 * ratings[GOOGLE_SCORE] + 0.25 * ratings[SENTIMENT_SCORE]
        if score > bestChildCareScoreOverall:
            bestChildCareScoreOverall = score
            bestChildCareOverall = care

    for library, ratings in librariesToReviewsCondensed.items():
        score = 0.75 * ratings[GOOGLE_SCORE] + 0.25 * ratings[SENTIMENT_SCORE]
        if score > bestLibraryScoreOverall:
            bestLibraryScoreOverall = score
            bestLibraryOverall = library

    for school, ratings in schoolsToReviewsCondensed.items():
        score = 0.75 * ratings[GOOGLE_SCORE] + 0.25 * ratings[SENTIMENT_SCORE]
        if score > bestSchoolScoreOverall:
            bestSchoolScoreOverall = score
            bestSchoolOverall = school

    bestChildCareScoreHouse = 0
    bestLibraryScoreHouse = 0
    bestSchoolScoreHouse = 0

    for care in childCare:
        ratings = childCareToReviewsCondensed[care]
        score = 0.75 * ratings[GOOGLE_SCORE] + 0.25 * ratings[SENTIMENT_SCORE]
        if score > bestChildCareScoreHouse:
            bestChildCareScoreHouse = score
    for library in libraries:
        ratings = librariesToReviewsCondensed[library]
        score = 0.75 * ratings[GOOGLE_SCORE] + 0.25 * ratings[SENTIMENT_SCORE]
        if score > bestLibraryScoreHouse:
            bestLibraryScoreHouse = score
    for school in schools:
        ratings = schoolsToReviewsCondensed[school]
        score = 0.75 * ratings[GOOGLE_SCORE] + 0.25 * ratings[SENTIMENT_SCORE]
        if score > bestSchoolScoreHouse:
            bestSchoolScoreHouse = score
    
    libraryScore = bestLibraryScoreHouse / bestLibraryScoreOverall
    schoolScore = bestSchoolScoreHouse / bestSchoolScoreOverall
    childCareScore = bestChildCareScoreHouse / bestChildCareScoreOverall
    educationScore = 0.35 * libraryScore + 0.5 * schoolScore + 0.15 * childCareScore
    output = [libraryScore, schoolScore, childCareScore, educationScore] # houseLibrary / maxLibrary, houseSchool / maxSchool, houseChildCare / maxChildCare, *
    return output
    




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

    # print()
    # eduAPI = EducationAPI(None)
    # schoolsToHome = None
    # librariesToHome = None
    # childCareToHome = None
    # with open('childCareToHome', 'rb') as file:
    #     childCareToHome = pickle.load(file)
    # # with open('librariesToHome', 'rb') as file:
    # #     librariesToHome = pickle.load(file)
    # with open('schoolsToHome', 'rb') as file:
    #     schoolsToHome = pickle.load(file)

    # # Rating, Sentiment Score
    # #librariesToReviews = eduAPI.findSentimentRatingScore(librariesToHome)
    # schoolsToReviews = eduAPI.findSentimentRatingScore(schoolsToHome)
    # childCareToReviews = eduAPI.findSentimentRatingScore(childCareToHome)
    # with open('schoolsToReviews', 'wb') as file:
    #     pickle.dump(schoolsToReviews, file)
    # # with open('librariesToReviews', 'wb') as file:
    # #     pickle.dump(librariesToReviews, file)
    # with open('childCareToReviews', 'wb') as file:
    #     pickle.dump(childCareToReviews, file)
    # print()

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
    # if not os.path.exists('schoolsToHome') or not os.path.exists('librariesToHome') or not os.path.exists('childCareToHome'):
    #     readData("houses/houseData/novaHousesSchoolsClean.csv")
    # if not os.path.exists('schoolsToReviews') or not os.path.exists('librariesToReviews') or not os.path.exists('childCareToReviews'):
    #     scoreData()
    
# if __name__ == "__main__":
#     # readData("houses/houseData/novaHousesSchoolsClean.csv")
#     # scoreData()
#     getEducationData("4003 Whispering Ln, Annandale, VA 22003, USA")
    

    

