import UserConnection, playlistDataSelection
import json

global spotifyConnection, playlistsDatabase
spotifyConnection = UserConnection.userConnection()
playlistsDatabase = r"C:\Users\galve\.vscode\SAI\Data\playlistData.json"
   
def getPlaylistTypeData(choice):
    with open(playlistsDatabase) as playlistJsonData:
        playlistsData = json.load(playlistJsonData)
        
    playlistTypes = {
        0 : "Vibes",
        1 : "Energy",
        2 : "Reggeton",
        3 : "isSpanishVibes",
        4 : "isAsia",
        5 : "isGym" 
    }
    
    songData = playlistsData[playlistTypes[choice]]
    
    def getSeed(songID):
        songRec = spotifyConnection.recommendations(seed_tracks=[songID], limit=1)
        return songRec['tracks'][0]['id']
    
    recommendationSeed = list(map(getSeed, songData))
        
    return recommendationSeed
        
    
