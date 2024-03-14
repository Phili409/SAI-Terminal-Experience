import UserConnection
import json, os

global spotifyConnection, currentUser 
spotifyConnection = UserConnection.userConnection()
currentUser = spotifyConnection.current_user()['id']
        
def selectPlaylist(playlistName):
    playlists = spotifyConnection.current_user_playlists()

    playlistMap = {playlist['name'] : playlist['id'] for playlist in playlists['items']}
    
    return playlistMap.get(playlistName)

def getPlaylistData(playID):
    limit = 100
    offset = 0
    counter = 0
    
    songsIDs = set()
    
    while True:
        selectedPlaylist = spotifyConnection.user_playlist_tracks(user=currentUser, playlist_id=playID, limit=limit, offset=offset)

        for song in selectedPlaylist['items']:
            songsIDs.add(song['track']['id'])
            counter += 1
            
        if len(selectedPlaylist['items']) <= 0:
            break 
        offset += limit
    return songsIDs
    
def updateMasterDatabase():
    databaseLocation = r"C:\Users\galve\.vscode\SAI\Data\database.json"
    lastOffset = r"C:\Users\galve\.vscode\SAI\Data\offset.txt"
    
    with open(databaseLocation) as file:
        databaseCurrentData = json.load(file)
        
    databaseCurrentData = set(databaseCurrentData)
    IDs = set()
    
    limit = 20
    
    if not (os.path.getsize(lastOffset) == 0) :
        offset = int(lastOffset.strip())
    else:
        offset = 0
        
    counter = 0 
        
    while True:
        userLikedSongs = spotifyConnection.current_user_saved_tracks(limit=limit, offset=offset)
        for likedSong in userLikedSongs['items']:
                IDs.add(likedSong['track']['id'])
                counter += 1
            
        if len(userLikedSongs['items']) <= 0:
            break 
        
        offset += limit
    
    newData = databaseCurrentData.union(IDs)
    
    with open(lastOffset, "w") as Offset:
        Offset.write(len(newData))
    
    with open(databaseLocation, 'w') as database:
        database.write(json.dumps(list(newData)))
        
def updatePlaylistDatabase(playlistName):
    playlistJsonData = r"C:\Users\galve\.vscode\SAI\Data\playlistData.json"
    playlistsNames = ["Vibes", "Energy", "Reggeton", "isSpanishVibes", "isAsia", "isGym"]
    
    with open(playlistJsonData) as file:
        playlistsData = json.load(file)
    
    storedData = playlistsData[playlistName] 
    currentData = set(getPlaylistData(selectPlaylist(playlistName)))
    
    newData = currentData.union(set(storedData))
    
    playlistsData[playlistName] = list(newData)
    
    with open(playlistJsonData, 'w') as playlistDatabase:
        playlistDatabase.write(json.dumps(playlistsData))
    
