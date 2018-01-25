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

def DEMO ():

    dice = [0, 0]
    sum_of_dice = roll_action (dice)
    points = 0
    if sum_of_dice ==2 or sum_of_dice ==3 or sum_of_dice ==12:
            print "The numbers of two dices are",dice
            print "The sum of two dices is",sum_of_dice
            print "It is LOSE !"

    if  sum_of_dice == 7 or sum_of_dice ==11:
            print "The numbers of two dices are",dice
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
DEMO ()

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

print "The demonstraion of the Craps for one round:"
print DEMO
print "The winning rate is about",win/100000.0
   
main()   
