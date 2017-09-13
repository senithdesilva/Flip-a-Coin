import random

class Coin:
    #initial flip is Heads
    def __init__(self):
        self.__side = 'Heads'

    #toss the coin funcation
    def toss_coin(self):
        if random.randint(0,1) == 0:
            self.__side = 'Heads'
        else:
            self.__side = 'Tails'

    #get toss funcation, returns the flipped side
    def get_coin(self):
        return self.__side
