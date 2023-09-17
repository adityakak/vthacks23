import pandas as pd
from pathlib import Path
import os

def getPhotoData(address):
    """Extracts photos from the given address"""
    dataPath = Path(os.path.join(os.getcwd(), "houses/houseData/novaHousesSchoolsClean.csv"))
    df = pd.read_csv(dataPath)
    df = df[df['abbreviatedAddress'] == address]
    photoLink = df.iloc[0]['photos/0']
    return photoLink