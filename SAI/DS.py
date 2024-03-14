import json, numpy
import UserConnection
from sklearn.cluster import KMeans

global userConnection, masterDatabasePath, kmeansRepository
userConnection = UserConnection.userConnection()
masterDatabasePath = r"C:\Users\galve\.vscode\SAI\Data\database.json"
kmeansRepository = r"C:\Users\galve\.vscode\SAI\Data\kmeans.json"


def getSongFeatures():
    with open(masterDatabasePath) as masterDatabase:
        masterData = json.load(masterDatabase)
    
    limit = 100
    offset = 0
        
    betaData = {
        "danceability" : [],
        "energy" : [],
        "key" : [],
        "loudness" : [],
        "liveness" : [],
        "valence" : [],
        "tempo" : []
    }
    
    danceabilityList = betaData["danceability"]
    energyList = betaData["energy"]
    keyList = betaData["key"]
    loudnessList = betaData["loudness"]
    livenessList = betaData["liveness"]
    valenceList = betaData["valence"]
    tempoList = betaData["tempo"]

    while offset < len(masterData):
        tracks = masterData[offset:(offset + limit)]
        extractedFeatures = userConnection.audio_features(tracks=tracks)
        
        for feature in extractedFeatures:
            danceabilityList.append(feature["danceability"])
            energyList.append(feature["energy"])
            keyList.append(feature["key"])
            loudnessList.append(feature["loudness"])
            livenessList.append(feature["liveness"])
            valenceList.append(feature["valence"])
            tempoList.append(feature["tempo"])

        offset += limit
        
    return betaData

def fitDataToCluster(dataList):    
    fittedList = numpy.array(dataList).reshape(-1, 1)
    
    kmeansClusters = KMeans(n_clusters=1, n_init=10)
    kmeansClusters.fit(fittedList)
    
    return kmeansClusters.cluster_centers_

def getDataMetricsFromClusters():
    featuresDictionary = getSongFeatures()
    
    aa = []
    for key in featuresDictionary.keys():
        aa.extend(featuresDictionary[key])
    
    clusterDataHashMap = {
        "danceability" : None,
        "energy" : None,
        "key" : None,
        "loudness" : None,
        "liveness" : None,
        "valence" : None,
        "tempo" : None,
    }
    
    clusterData = list(map(fitDataToCluster ,aa))
    
    for index, key in enumerate(clusterDataHashMap.keys()):
        clusterDataHashMap[key] = clusterData[index].tolist()
    
    with open(kmeansRepository, "w") as repository:
        json.dump(clusterDataHashMap, repository)


def getMetrics():
    with open(kmeansRepository) as repository:
        metrics = json.load(repository)
    return metrics 

def getMinMaxMedium():
    data = getSongFeatures()
    returnData = {
        "danceability" : None,
        "energy" : None,
        "key" : None,
        "loudness" : None,
        "liveness" : None,
        "valence" : None,
        "tempo" : None
    }
    
    for key, value in data.items():
        MIN = min(*value)
        MAX = max(*value)
        MEAN = sum(value) / len(value)
        returnData[key] = [MIN, MEAN, MAX] 
    return returnData
        




