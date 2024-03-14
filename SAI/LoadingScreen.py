import sys, time, threading, cursor, msvcrt, time
from Input import Input
from TerminalPosition import TerminalPosition
from TerminalTemplates import TerminalTemplates

class Loading:
    def __init__(self):
        self.TerminalTemplate = TerminalTemplates.Return(self=TerminalTemplates(), template="Loading")
        self.ToggleBlink = True
    
    def toggle(self):
        if self.ToggleBlink: self.ToggleBlink = False
        else: self.ToggleBlink = True
        
    def Animation(self):
        x = 30
        while self.ToggleBlink:
            cursor.hide()
            for _ in range(6): 
                TerminalPosition.UpdatePosition(x=x , y=4)
                TerminalPosition.Delete(amount=1)
                x -= 1
                time.sleep(1)
            for _ in range(6):
                TerminalPosition.Print(x=x ,y=4, text=".")
                x += 1
                time.sleep(1)
    
    def Return_Loading_Screen(self):
        print(self.TerminalTemplate)
        self.Animation()



            
        
        