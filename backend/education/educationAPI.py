import pandas as pd

class School():
    def __init__(self, schoolName, schoolRating):
        self.schoolName = schoolName
        self.schoolRating = schoolRating

class EducationAPI():
    def __init__(self, dfRow):
        self.data = dfRow
        self.homeStatus = self.data['homeStatus']
        self.city = self.data['address/city']
        self.street = self.data['address/streetAddress']
        self.state = self.data['address/state']
        self.zipCode = self.data['address/zipcode']
        self.elementarySchool = School(self.data['schools/0/name'], self.data['schools/0/rating'])
        self.middleSchool = School(self.data['schools/1/name'], self.data['schools/1/rating'])
        self.highSchool = School(self.data['schools/2/name'], self.data['schools/2/rating'])

    def getReviews(self):
        return self.data['reviews']