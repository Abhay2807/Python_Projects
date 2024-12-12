class Board:

    def __init__(self):
        self.board=[' ',' ',' ',
                    ' ',' ',' ',
                    ' ',' ',' ',]
        

    def print_board(self):
            print("\n")
            print("Our game Board")
            print("\n")
            print(' '+self.board[0]+' | '+self.board[1]+' | '+self.board[2])
            print("----------")
            print(' '+self.board[3]+' | '+self.board[4]+' | '+self.board[5])
            print("----------")
            print(' '+self.board[6]+' | '+self.board[7]+' | '+self.board[8])
            print("\n")
            print("\n")

    def update_board(self,position,type):
        if(self.board[position-1]==" "):
            self.board[position-1] = type
            y=len(self.board)
            empty_positions=[]
            for x in range(y):
                if(self.board[x]==" "):
                    empty_positions.append(x+1)
            print(f"Currently free positions are {empty_positions}")
            return  True
        else:
            print("Position already filled. Try another position.")
            y=len(self.board)
            empty_positions=[]
            for x in range(y):
                if(self.board[x]==" "):
                    empty_positions.append(x+1)
            print(f"Currently free positions are {empty_positions}")
            return False
        
    def check_winner(self,type):
        if(self.board[0]==type and self.board[1]==type and self.board[2]==type) or \
        (self.board[3]==type and self.board[4]==type and self.board[5]==type) or \
        (self.board[6]==type and self.board[7]==type and self.board[8]==type) or \
        (self.board[0]==type and self.board[3]==type and self.board[6]==type) or \
        (self.board[1]==type and self.board[4]==type and self.board[7]==type) or \
        (self.board[2]==type and self.board[5]==type and self.board[8]==type) or \
        (self.board[0]==type and self.board[4]==type and self.board[8]==type) or \
        (self.board[2]==type and self.board[4]==type and self.board[6]==type):
            return True
        else:
            return False
        
    def check_draw(self):
        if " " not in self.board:
            return True
        else:
            return False

class Player():
     
    def __init__(self,type):
        self.type=type
        self.name=self.get_player_name()


    def get_player_name(self):
        if(self.type=='X'):
            player_name=input("Player with 'X' Move, enter your name: ")
        else:
            player_name=input("Player with 'O' Move, enter your name: ")

        return player_name
    
class Game:
    def __init__(self):
        self.board=Board()
        self.board.print_board()
        self.player1=Player('X')
        self.player2=Player('O')
        print(f"Name of player  '{self.player1.type}'  is : {self.player1.name}")
        print(f"Name of player  '{self.player2.type}'  is : {self.player2.name}")

        self.current_player=self.player1    
        

    def play_game(self):
        print("Let's Play TIC TAC TOE GAME")
        print("Game Started")
        
        while True:
            print("Game in Progress")
            print(f"Currently player '{self.current_player.type}' is playing")

            select_position=(f"Select One Position among [1-9] player '{self.current_player.type}' : ")
            position=int(input(select_position))

            if position in range(1,10):

                if(self.board.update_board(position,self.current_player.type)):
                    self.board.print_board()

                    if(self.board.check_winner(self.current_player.type)):
                        print(f"Congratulations Player '{self.current_player.type}' : {self.current_player.name} \nYou've won the game.")
                        break

                    elif(self.board.check_draw()):
                        print("It's a Draw!")
                        break

                    else:
                        if(self.current_player==self.player1):
                            self.current_player=self.player2
                        else:
                            self.current_player=self.player1

            else:
                print("Enter valid Position Number between 1  and 9 ")


         
game=Game()
game.play_game()






            
