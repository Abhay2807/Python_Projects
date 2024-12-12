import random

class Game:
    
    def __init__(self):
        self.computer_move=self.get_computer_move()
        self.user_move=self.get_user_move()
        self.result=self.get_result()

    def get_computer_move(self):
        random_num=random.randint(1,3)

        options={
            1:'rock',
            2:'paper',
            3:'scissors'
        }

        return options[random_num]
    
    def get_user_move(self):

        while True:
            user_input=input("Enter one among the following: rock/paper/scissors ")

            if (user_input.lower()) in ['rock','paper','scissors']:
                break
            else:
                print("Invalid input. Please enter rock, paper, or scissors.")

        return user_input.lower()
    
    def get_result(self):
        if self.computer_move==self.user_move:
            return "draw"
        
        elif (self.user_move=="rock" and self.computer_move=="scissors"):
            return "win"
        
        elif(self.user_move=="paper" and self.computer_move=="rock"):
            return "win"
        
        elif(self.user_move=="scissors" and self.computer_move=="paper"):
            return "win"
        
        else:
            return "lose"
        

    def game_result(self):
        print(f"Computer's Move is : {self.computer_move}")
        print(f"User's Move is : {self.user_move}")

        if(rps_game.result=="win"):
            print(f"User Wins as {self.user_move} beats {self.computer_move} ,IN RPS Game")
        elif(rps_game.result=="lose"):
            print(f"Computer Wins as {self.computer_move} beats {self.user_move} ,IN RPS Game")
        else:
            print("It's a Draw!")


while True:
    rps_game=Game()
    rps_game.game_result()

    play_again=input("Do you want to play again? (yes/no): ")

    if play_again.lower()!="yes":
        break

