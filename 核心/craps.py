##The following description has been adopted from Deitel & Deitel.
##One of the most popular games of chance is a dice game called "craps,"
##which is played in casinos and back alleys throughout the world.
##The rules of the game are straightforward:
##
##A player rolls two dice. Each die has six faces.
##These faces contain 1, 2, 3, 4, 5, and 6 spots.
##After the dice have come to rest, the sum of the spots on the
##two upward faces is calculated.
##If the sum is 7 or 11 on the first throw, the player wins.
##If the sum is 2, 3, or 12 on the first throw (called "craps"),
##the player loses (i.e. the "house" wins). If the sum is 4, 5, 6, 8, 9, or 10
##on the first throw, then the sum becomes the player's "point."
##To win, you must continue rolling the dice until you "make your point."
##The player loses by rolling a 7 before making the point.
##
##Write a program that implements a craps game according to the above rules.
##The game should allow for wagering. This means that you need to prompt that user
##for an initial bank balance from which wagers will be added or subtracted.
##Before each roll prompt the user for a wager. Once a game is lost or won,
##the bank balance should be adjusted. As the game progresses, print various messages
##to create some "chatter" such as, "Sorry, you busted!", or "Oh, you're going for broke, huh?",
##or "Aw cmon, take a chance!", or "You're up big, now's the time to cash in your chips!"

import random

def roll_die ():
    roll = random.randint(1,6)
    return roll

def roll_two_die (dice):
    dice[0] = roll_die ()
    dice[1] = roll_die ()

def sum_dice (dice):
    sum_of_dice = dice[0] + dice[1]
    return sum_of_dice

def roll_action (dice):
    roll_two_die (dice)
    sum_of_dice = sum_dice (dice)
    return sum_of_dice

def main ():
##    die1 = roll_die ()
##    die2 = roll_die ()

    dice = [0, 0]
    sum_of_dice = roll_action (dice)
    point = sum_of_dice

##    print die1, die2
    print dice
    print sum_of_dice
    print point

main ()
    
