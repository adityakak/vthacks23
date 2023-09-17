import pandas as pd
from pathlib import Path
import os
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def getPhotoData(address):
    """Extracts photos from the given address"""
    dataPath = Path(os.path.join(os.getcwd(), "houses/houseData/novaHousesSchoolsClean.csv"))
    df = pd.read_csv(dataPath)
    df = df[df['abbreviatedAddress'] == address]
    photoLink = df.iloc[0]['photos/0']
    return photoLink

def getHomesLink(address):
    driver = webdriver.Chrome()
    driver.get("https://www.homes.com")
    # input_element = driver.find_element(By.ID,"ta-byah")
    # input_element = driver.find_element_by_id('ta-byah')
    input_element = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    # input_element.clear()
    time.sleep(5)
    input_element.send_keys(address)
    input_element.send_keys(Keys.ENTER)
    time.sleep(5)
    currentURL = driver.current_url
    return currentURL

def scoreAllHouses():
    dataPath = Path(os.path.join(os.getcwd(), "houses/houseData/novaHousesSchoolsClean.csv"))
    df = pd.read_csv(dataPath)
    for index, row in df.iterrows():
        address = row['abbreviatedAddress']
        photoLink = getPhotoData(address)
        print(f"Photo Link: {photoLink}")
        homesLink = getHomesLink(address)
        print(f"Homes Link: {homesLink}")
        break