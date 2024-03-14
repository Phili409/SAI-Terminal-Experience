class TerminalTemplates(object):
    def __init__(self):
        self.TemplateMap:dict = {}
        self.TemplateFiles:list = [
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\CreatePlaylist.txt", 
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\DeletePlaylists.txt", 
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\Loading.txt", 
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\MainMenu.txt", 
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\MainMenuSelection.txt", 
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\Play.txt", 
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\PlayAni.txt", 
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\PlaylistRec.txt",
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\playlistSelector.txt",
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\SongSelector.txt",
            r"C:\Users\galve\.vscode\SAI\Data\Terminal Templates\UpdateData.txt"
            ]
        self.TemplateName:list = [
            "Create Playlist", 
            "Delete Playlists", 
            "Loading", 
            "Main Menu", 
            "Main Menu Selection", 
            "Play", 
            "Play Animation", 
            "Playlist Recomendation", 
            "Playlist Selector", 
            "Song Selector", 
            "Update Data"
            ]
    
    def ParseTemplates(self):
        for index in range(len(self.TemplateName)):
            with open(self.TemplateFiles[index], "r") as file:
                FileLines = file.read()
            self.TemplateMap[self.TemplateName[index]] = FileLines
    
    def Return(self, template):
        self.ParseTemplates()
        return self.TemplateMap[template]
            