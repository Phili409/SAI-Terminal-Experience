import UserConnection
import json

global saiCreatedPlaylists, userConnection
saiCreatedPlaylists = r"C:\Users\galve\.vscode\SAI\Data\linkedPlaylists.json"
userConnection = UserConnection.userConnection()


def updateLinkedPlaylists(playlistID):
    with open(saiCreatedPlaylists) as file:
        currentCreatedPlaylists = json.load(file)
    
    currentCreatedPlaylists["listOfPlaylists"].append(playlistID)
    
    
    with open(saiCreatedPlaylists, 'w') as file:
        json.dump(currentCreatedPlaylists, file)

def linkedPlaylists():
    with open(saiCreatedPlaylists) as file:
        currentPlaylistData = json.load(file)
        
    linkedPlaylists = currentPlaylistData["listOfPlaylists"]
    return linkedPlaylists

def deleteCreatedPlaylists(listOfIDs):
    queue = listOfIDs
    
    while not (len(queue) <= 0):
        ID = queue.pop(0)
        userConnection.user_playlist_unfollow(user=userConnection.current_user()['id'],playlist_id=ID)
        
    with open(saiCreatedPlaylists, "w") as file:
        json.dump({"listOfPlaylists": []}, file)
        
        
