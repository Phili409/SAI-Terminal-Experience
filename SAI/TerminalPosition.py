import sys
class TerminalPosition:
    def __init__(self):
        pass
    
    @staticmethod
    def Up(RowAmount:int=1):
        sys.stdout.write(f'\033[{RowAmount}A')
        sys.stdout.flush()
        
    @staticmethod
    def Down(RowAmount:int=1):
        sys.stdout.write(f'\033[{RowAmount}B')
        sys.stdout.flush()
        
    @staticmethod
    def Right(ColumnAmount:int=1):
        sys.stdout.write(f'\033[{ColumnAmount}C')
        sys.stdout.flush()
    
    @staticmethod
    def Left(ColumnAmount:int=1):
        sys.stdout.write(f'\033[{ColumnAmount}D')
        sys.stdout.flush()
    
    @staticmethod
    def UpdatePosition(x, y):
        sys.stdout.write(f'\033[{y};{x}H')
        sys.stdout.flush()
        
    @staticmethod
    def ClearLine(position=-1):
        if position == -1:
            sys.stdout.write('\033[K')
            sys.stdout.flush()
        else:
            sys.stdout.write(f'\033[{position}K')
            sys.stdout.flush()
    @staticmethod
    def Delete(amount:int):
        sys.stdout.write(f'\b'+' '*amount +'\b')
        sys.stdout.flush()  
              
    @staticmethod
    def Print(x:int, y:int, text:str):
        TerminalPosition.UpdatePosition(x, y)
        sys.stdout.write(text)
        sys.stdout.flush()
