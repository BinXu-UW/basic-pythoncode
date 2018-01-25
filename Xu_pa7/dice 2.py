import random
import datetime

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

def getNow():   
    return datetime.datetime.now()

def main ():
   strat = getNow()
   total = 0
   for i in range(100000):
       dice = [0, 0]
       sum_of_dice = roll_action (dice)
       points = 0
       if sum_of_dice ==2 or sum_of_dice ==3 or sum_of_dice ==12:
            status =0
       if  sum_of_dice == 7 or sum_of_dice ==11:
            status = 1              
       elif sum_of_dice !=2 and sum_of_dice !=3 and sum_of_dice !=12 and sum_of_dice !=7 and sum_of_dice !=11:
            while points !=7 and points !=sum_of_dice:
                points = roll_action (dice)
                if points == 7 :
                    status = 0
                if points == sum_of_dice:
                    status = 1
                    
       total =total+status   
   print total/100000.0
   end = getNow();
   print end - strat
   
    
main()   
