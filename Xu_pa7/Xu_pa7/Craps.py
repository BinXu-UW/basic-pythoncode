# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 6
# Filename: Craps.py
# Date Created: 4/21/2010
# Description: This program simulat the craps game, it will show a demonstration 
#              of a round and it will calculate the winning rate of this game             
import random


# Programmer: BX
# Class: CptS 111
# Function Name: roll_dice ()
# Date Created: 4/21/2010
# Description: This function set a dice and make it rolling 
# Parameters: 
# Preconditions: 
# Postconditions:
def roll_dice ():
    roll = random.randint(1,6)
    return roll

# Programmer: BX
# Class: CptS 111
# Function Name: roll_two_dice (dice)
# Date Created: 4/21/2010
# Description: This function set two dice and use the rolling function
# Parameters: 
# Preconditions: 
# Postconditions:
def roll_two_dice (dice):
    dice[0] = roll_dice ()
    dice[1] = roll_dice ()
    
# Programmer: BX
# Class: CptS 111
# Function Name: sum_dice (dice)
# Date Created: 4/21/2010
# Description: This function calculate the sum of two dices
# Parameters: 
# Preconditions: 
# Postconditions:
def sum_dice (dice):
    sum_of_dice = dice[0] + dice[1]
    return sum_of_dice

# Programmer: BX
# Class: CptS 111
# Function Name: roll_action (dice)
# Date Created: 4/21/2010
# Description: This function dirves the rolling part
# Parameters: 
# Preconditions: 
# Postconditions:
def roll_action (dice):
    roll_two_die (dice)
    sum_of_dice = sum_dice (dice)
    return sum_of_dice


# Programmer: BX
# Class: CptS 111
# Function Name: main()
# Date Created: 4/21/2010
# Description: This function drives the Craps program
# Parameters: 
# Preconditions: 
# Postconditions:
def main ():
   win = 0
   count = 0
   while(count<=100000):
       count+=1;
       dice = [0, 0]
       sum_of_dice = roll_action (dice)
       points = 0
       if sum_of_dice ==2 or sum_of_dice ==3 or sum_of_dice ==12:
           pass
       if  sum_of_dice == 7 or sum_of_dice ==11:
            win+=1             
       elif sum_of_dice !=2 and sum_of_dice !=3 and sum_of_dice !=12 and sum_of_dice !=7 and sum_of_dice !=11:
            while points !=7 and points !=sum_of_dice:
                points = roll_action (dice)
                if points == 7 :
                    pass
                if points == sum_of_dice:
                    win+=1
   
   print "The winning rate of this game is about",win/100000.0
   

# Programmer: BX
# Class: CptS 111
# Function Name: main()
# Date Created: 4/21/2010
# Description: This function demonstrate the game, it is similar with main()
# Parameters: 
# Preconditions: 
# Postconditions:
def demo ():
    print "The demonstraion of the Craps for one round:"
    dice = [0, 0]
    sum_of_dice = roll_action (dice)
    points = 0
    if sum_of_dice ==2 or sum_of_dice ==3 or sum_of_dice ==12:
            print "The initial roll numbers of two dices are",dice
            print "The sum of two dices is",sum_of_dice
            print "It is LOSE !"

    if  sum_of_dice == 7 or sum_of_dice ==11:
            print "The initial roll numbers of two dices are",dice
            print "The sum of two dices is",sum_of_dice
            print "It is WIN !"
              
    elif sum_of_dice !=2 and sum_of_dice !=3 and sum_of_dice !=12 and sum_of_dice !=7 and sum_of_dice !=11:
         print "The initial roll numbers of two dices are",dice
         print "The sum of two dices is",sum_of_dice
         while points !=7 and points !=sum_of_dice:
               points = roll_action (dice)
               if points == 7 :
                    print "The initial roll didn't WIN or LOSE, then do the reroll untill we get a result"
                    print "The fianl reroll numbers of two dices are",dice
                    print "The sum of two dices is",points
                    print "The fianl reroll is 7 which means LOSE !"

               if points == sum_of_dice:
                    print "The initial roll didn't WIN or LOSE, then do the reroll untill we get a result"
                    print "The fianl reroll numbers of two dices are",dice
                    print "The sum of two dices is",points
                    print "The fianl reroll is equal to the initial roll which means WIN !"

    
temp = 0;
if(temp == 0):
    temp+=1
    demo();
    print "///////////////////////////////////"
main ()

