import Coin
import sys

def main():
    flip_coin = Coin.Coin()

    #initial flip is heads
    print('The flipped side is:', flip_coin.get_coin())

    print('flipping the coin!')
    flip_coin.toss_coin()

    print('The flipped side is:', flip_coin.get_coin(),'\n')

def replay():
    print('Do you wish to play again?')
    while True:
        play = input('If YES, press (y). If NO, press (n): \n')
        if play == 'y':
                   print('Lets Start Playing!\n')
                   main()
        elif play == 'n':
                   print('Thank you for playing')
                   print('See you soon')
                   sys.exit() #the program will stop. 
        else:
            print('Please Re-enter') #validation

main()
replay()
