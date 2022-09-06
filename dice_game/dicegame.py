from sys import *
import sys as sys
from random import randint

class RollDice():

    def input_number(): 
        print("type a number between 1-6")
        input_num = int(input())
        if input_num < 1 or input_num > 6:
            print("input number out of range, please type a number between 1-6")
            sys.exit()
        return input_num   

    def rand_number():
        rand_num = randint(1,6)
        print(rand_num)
        return rand_num

    

    if input_number() == rand_number():
        print("Congratulations, you won !")    
    else:
        print("Sorry you lost !")
    






