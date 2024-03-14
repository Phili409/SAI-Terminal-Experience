import TerminalPosition, Input, TerminalTemplates

class Main_Menu:
    @staticmethod
    def load_menu():
        menu_template = TerminalTemplates.TerminalTemplates.Return(self=TerminalTemplates.TerminalTemplates(), template="Main Menu Selection")
        print(menu_template)
    
    @staticmethod
    def start():
        Main_Menu.load_menu()
        
        TerminalPosition.TerminalPosition.UpdatePosition(x=0,y=4)
        menu_selection = Input.Input.Return(self=Input.Input(), v_=0, validation_condition=("int", 5))
        return menu_selection
        
        
            

