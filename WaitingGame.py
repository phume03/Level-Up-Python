#!/usr/bin/env python
# @author: Phumelela Mdluli
# @assignment: Level Up: Python - Waiting Game
# @date: 09/September/2024
# @description: test user reaction speed
# @python version: Python 3
# @notes:
from random import randint
from time import sleep
from time import perf_counter
import math

"""
Records how long it takes for a user to respond to an onscreen prompt.

Records how long it takes for a user to respond to an onscreen prompt by pressing the enter button.

Attributes:
    NONE

Methods:
    waiting_game():
        times how long it takes for a user to respond to an onscreen prompt.

"""
def waiting_game():
    """
    this function prints a message for the user to wait a random amount of time, 
    somewhere between two (2) to four (4) seconds. It records the time between
    two consecutive presses, by the user, of the enter button.

    Parameters
    ----------
    NONE

    Returns
    -------
    NONE

    """
    start_time: float = float(0)
    end_time: float = float(0)
    your_time: float = float(0)
    wait_interval = float(0)
    play: bool = True
    print(f'Welcome, we are playing "the waiting game".')
    print(f'Instructions: press Enter to start the timer. Wait the instructed amount of time. Then press enter again to stop the timer. You will be told if you waited just right, too long, or you were too hasty. Enjoy!')

    while (play==True):
        wait_interval: float = 2 + ( randint(0,20) / 10 )
        print(f'\nYou have to wait {wait_interval:.2f} seconds.')
        response = input("Press ENTER to start the timer.")
        start_time = perf_counter()
        response = input(f'Press ENTER to stop.')
        end_time= perf_counter()
        your_time = end_time - start_time
        if round(your_time,2) == round(wait_interval,2):
            print(f'Wow, you have swift fingers. You matched the wait time.\nYour Time: {your_time:.2f}\nWait Time: {wait_interval:.2f}')
        elif round(your_time,2) > round(wait_interval,2):
            if round(your_time, 2) - 0.25 < round(wait_interval,2):
                print(f'That was close! You waited a fraction of a second too long.\nYour Time: {your_time:.2f}\nWait Time: {wait_interval:.2f}\nTry to be faster next time.')
            else:    
                print(f'Okay, you waited a bit too long.\nYour Time: {your_time:.2f}\nWait Time: {wait_interval:.2f}\nTry to be faster next time.')
        else:
            if round(your_time, 2) + 0.25 > round(wait_interval,2):
                print(f'That was close! You were a fraction of a second too fast. Patience is a virtue.\nYour Time: {your_time:.2f}\nWait Time: {wait_interval:.2f}')
            else:
                print(f'Hmm, you were too fast there. Try to be more patient.\nYour Time: {your_time:.2f}\nWait Time: {wait_interval:.2f}')

        response = input("You can press ENTER to TRY AGAIN or type QUIT to EXIT.\n...  ")
        if response.upper() == "QUIT" :
            play = False
        else:
            play = True
    return

if __name__ == "__main__":
    """
    Run a Simple Test of Our Game
    """
    waiting_game()