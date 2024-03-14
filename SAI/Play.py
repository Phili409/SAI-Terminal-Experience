import sys, time, threading, cursor, msvcrt, time
from Input import Input
from TerminalPosition import TerminalPosition
from TerminalTemplates import TerminalTemplates
import UserConnection
class SAI_Queue:
    def __init__(self):
        self.Q = UserConnection.userConnection().queue()
    
    def Queue(self, song):
        UserConnection.userConnection().add_to_queue(uri=song)

class Play:
    def __init__(self):
        self.User = UserConnection.userConnection()
        self.Playing = False
        self.ShuffleToggle = False
        self.SongName = None
        self.PlaylistName = None
        self.PlayID = None
        self.SongLenght = 0
        self.CurrentSongLenght = 0
        self.TerminalTemplates = {
            "Loading": TerminalTemplates.Return("Loading"),
            "Play": TerminalTemplates.Return("Play"),
            "Play Animation": TerminalTemplates.Return("Play Animation"),
            "Playlist Selector": TerminalTemplates.Return("Playlist Selector"),
            "Song Selector": TerminalTemplates.Return("Song Selector")
            }
        self.SAI_Q = SAI_Queue()
        
    def Animation(self):
        pass 
    def Skip(self):
        self.User.next_track()
        
    def Shuffle(self):
        self.User.shuffle()
        
    def Back(self):
        self.User.previous_track()
        
    def Pause(self):
        self.User.pause_playback()
        
    def Play(self):
        self.User.start_playback()
    
    def CurrentSong(self):
        return self.User.currently_playing()
        
    def Actions(self):
        pass
    
    def UpdateDuration(self):
        pass
    def UpdateData(self):
        pass
    def GetSongData(self):
        pass
    def GetPlaylistData(self):
        pass
    def SelectSong(self):
        pass
    def SelectPlaylist(self):
        pass
    def Search(self):
        pass
    def PlaylistMenu(self):
        pass
    def MainGraphic(self):
        print(self.TerminalTemplates["Play"])
    def main(self):
        while True:
            self.MainGraphic()

if "a" == "a":
    app = Play()
    app.Skip()
