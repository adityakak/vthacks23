from pathlib import Path
import os
import pickle
dataPath = Path(os.path.join(os.getcwd(), 'envData/envData'))
with open(dataPath, 'rb') as file:
        data = pickle.load(file=file)
for i in data.keys():
    print(i+":"+str(data[i]))
