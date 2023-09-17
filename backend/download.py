import pickle

with open('schoolsToReviews', 'rb') as file:
    schoolsToReviews = pickle.load(file)
with open('librariesToReviews', 'rb') as file:
    librariesToReviews = pickle.load(file)
with open('childCareToReviews', 'rb') as file:
    childCareToReviews = pickle.load(file)
print()