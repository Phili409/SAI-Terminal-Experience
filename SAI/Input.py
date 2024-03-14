import sys, time, threading, cursor, msvcrt
import TerminalPosition
class Input:
    def __init__(self):
        self.StopBlinking = False
        self.Current = ""

    def BlinkingDot(self):
        while not self.StopBlinking:
            # Display current input along with the dots
            sys.stdout.write('\r' + self.Current + '.' * (26 - len(self.Current)))
            sys.stdout.flush()
            time.sleep(0.5)
            # Clear the dots without going to a new line
            sys.stdout.write('\r' + ' ' * (len(self.Current) + 26) + '\r' + self.Current)
            sys.stdout.flush()
            time.sleep(0.5)
    
    def reduce_3(self):
        patterns = ['...', '..', '.', ' ']
        index = 0
        while not self.StopBlinking:
            sys.stdout.write('\r' + self.Current + patterns[index])
            sys.stdout.flush()
            time.sleep(0.5)
            index = (index + 1) % 4  


    def CustomInput(self, prompt, condition=None):
        print(prompt, end="", flush=True)
        while True:
            ch = msvcrt.getch().decode('utf-8', 'ignore')
            if ch == '\r':  # Enter key
                match(condition[0]):
                    case (None):
                        print()
                        return self.Current
                    
                    case ("int"):
                        MAX = int(condition[1])
                        if self.Current.isdigit():
                            if int(self.Current) <= MAX: 
                                print()
                                return self.Current
                        
                        print("Invalid Choise", end="")
                        TerminalPosition.TerminalPosition.ClearLine()
                        
                    case ("str"):
                        if self.Current:
                            print()
                            return self.Current
                        
                        print("Invalid Inpit", end="")
                        TerminalPosition.TerminalPosition.ClearLine()
                        
                    case ("tupple"):
                        pass
                
            elif ch == '\b':  # Backspace key 
                if self.Current:
                    print(ch + ' ' + ch, end="", flush=True)
                    self.Current = self.Current[:-1]
            else:  
                print(ch, end="", flush=True)
                self.Current += ch

    def GetInput(self, condition=None):
        sys.stdout.write('\033[1B\r')  # Move down one line and return to the beginning
        sys.stdout.flush()
        result = self.CustomInput("", condition=condition)
        self.StopBlinking = True
        return result

    def Return(self, v_:int, validation_condition:tuple=None):
        cursor.hide()
        thread = threading.Thread(target=self.BlinkingDot) if v_ == 1 else threading.Thread(target=self.reduce_3)
        thread.start()
        user_input = self.GetInput(condition=validation_condition)
        sys.stdout.write('\033[1A\r                 \r')  # Move up one line and clear it
        sys.stdout.flush()
        cursor.show()
        return user_input