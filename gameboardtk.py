class BoardClass:
    '''Attributes:
Players user name
User name of the last player to have a turn
Number of wins
Number of ties
Number of losses'''
#Default constructor
    def __init__(self,player_symb:str=''):
        self.wins=0
        self.ties=0
        self.losses=0
        self.last_player=None
        self.symbol=player_symb
        self.symbol_dict = {"A1":' ',"B1":' ',"C1":' ',"A2":' ',"B2":' ',"C2":' ',"A3":' ',"B3":' ',"C3":' '}
        self.play=self.wins+self.losses+self.ties

#To draw the game board
    '''def draw_gameboard(self):  
        row_one =  '  | ' + self.symbol_dict['1']
        row_one += '   | ' + self.symbol_dict['2']
        row_one += '   | ' + self.symbol_dict['3']
        print(row_one)

        print('==|====|====|==')

        row_two =  '  | ' + self.symbol_dict['4']
        row_two += '   | ' + self.symbol_dict['5']
        row_two += '   | ' + self.symbol_dict['6']
        print(row_two)

        print('==|====|====|==')

        row_three =  '  | ' + self.symbol_dict['7']
        row_three += '   | ' + self.symbol_dict['8']
        row_three += '   | ' + self.symbol_dict['9']
        print(row_three, "\n")'''

#To update the game board after each turn 
    '''def updateGameBoard(self,grid_coord,player_symb):
        keys1=self.symbol_dict.keys()
        keys=list(keys1)
        if grid_coord in keys:
            if self.symbol_dict[grid_coord] == '':
                self.symbol_dict[grid_coord] = player_symb
                return True
            else:
                print('Place Filled! Try entering into another place')
                return False
        else:
            print('Invalid Choice! Try Again with a number from 1-9(both included)')
            return False'''
        

#To reset the game board at the end of each game to a blank game board
    def resetGameBoard(self,g):
            g = {'A1':'','B1':'','C1':'','A2':'','B2':'','C2':'','A3':'','B3':'','C3':''}
            
#To keep a count of the number of games played
    def updateGamesPlayed(self):
        self.play=self.play+1
        return self.play

#To check who if either of the players have won the game 
    def isWinner(self,g):
        symbol = self.symbol
        
        
        if g[0] == symbol and g[1] == symbol and g[2] == symbol:
            return True
            self.wins+=1
        elif g[3] == symbol and g[4] == symbol and g[5] == symbol:
            return True   
            self.wins+=1
        elif g[6] == symbol and g[7] == symbol and g[8] == symbol:
            return True 
            self.wins+=1
        elif g[0] == symbol and g[3] == symbol and g[6] == symbol:
            return True 
            self.wins+=1
        elif g[1] == symbol and g[4] == symbol and g[7] == symbol:
            return True 
            self.wins+=1
        elif g[2] == symbol and g[5] == symbol and g[8] == symbol:
            return True
            self.wins+=1
        elif g[2] == symbol and g[4] == symbol and g[6] == symbol:
            return True 
            self.wins+=1
        elif g[0] == symbol and g[4] == symbol and g[8] == symbol:
            return True 
            self.wins+=1
        else:
            return False
            self.losses+=1

#To check if the game has tied 
    def boardIsFull(self,g):
        num_blanks = 0
        #g=list(self.symbol_dict.values())
        for i in g:
                if i == " ":
                    num_blanks += 1
        # if the player didn't win and no spaces are left, it's a draw
        if self.isWinner(g) == False and num_blanks == 0:
            return True
            self.ties+=1
        else:
            return False

#To find who played the last hand 
    def set_lastplayer(self,lastplayername):
        self.last_player=lastplayername
        return lastplayername

#To print the statistics of the game 
    def printStats(self):
        y=self.updateGamesPlayed()
        
        a=y
        b=self.last_player
        w=self.wins
        c=w
        d=self.losses
        e=self.ties
        return[a,b,c,d,e]
