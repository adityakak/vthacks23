import pandas as pd
from pathlib import Path
import os

def load_data(dataPath : Path):
    df = pd.read_csv(dataPath)

    dropWord = "maps.googleapis.com"
    df = df[~df['photos/0'].str.contains(dropWord)]


    newFileName = dataPath.stem + "Clean" + dataPath.suffix
    newFilePath = dataPath.parent / newFileName
    df.to_csv(newFilePath, index=False)

if __name__ == "__main__":
    dataPath = Path(os.path.join(os.getcwd(), "houses/houseData/novaHouses.csv"))
    load_data(dataPath)    