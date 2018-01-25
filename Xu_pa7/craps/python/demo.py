import random

def roll_dice ():
    roll = random.randint(1,6)
    return roll

def roll_two_dice (dice):
    dice[0] = roll_dice ()
    dice[1] = roll_dice ()

def sum_dice (dice):
    sum_of_dice = dice[0] + dice[1]
    return sum_of_dice

def roll_action (dice):
    roll_two_dice (dice)
    sum_of_dice = sum_dice (dice)
    return sum_of_dice
