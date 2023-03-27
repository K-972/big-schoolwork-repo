from msilib.schema import SelfReg
import random
from typing import Self

from sklearn.semi_supervised import SelfTrainingClassifier

class rock_paper_scissors:

    def start(self):
        global ai_option

        optipons = ['Rock', 'Paper', "Scissors"]

        ran_num = random.randint(0, 2)
        ai_option = optipons[ran_num]
        ai_option.lower()
        print(ai_option)
        #print(ran_num)

    def get_user_input(self):
        global user_input
        user_input = input("Rock, Paper or Scissors")
        user_input = user_input.lower()
    def win_conditions(self, user_input, ai_option):
        if user_input == ai_option:
            print('draw')

        elif user_input == 'scissors' and ai_option == "rock":
            print("computer wins")
        elif user_input == 'rock' and ai_option == "scissors":
            print("computer wins")
        elif user_input == 'paper' and ai_option == 'scissors':
            print('computer wins')

        # human wins

        elif user_input == 'paper' and ai_option == 'rock':
            print('you win')
        elif user_input == 'scissors' and ai_option == 'paper':
            print('you win')
        elif user_input == 'rock' and ai_option == 'scissors':
            print('you win')

rock_paper_scissors.start(SelfTrainingClassifier)

rock_paper_scissors.get_user_input(SelfReg)
rock_paper_scissors.win_conditions(Self, user_input, ai_option)




