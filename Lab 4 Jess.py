########################################################################
##
## CS 101 Lab
## Program #4
## Name Jessica Burkhart
## Email jcbc2b@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random #this line is to import random so that later I can get generate a random number

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    x = True #this line is to set x to True
    while x: #this line is to make the while loop run when x is true
        play = input('Do you want to play again? ==> ') #this line asks the user for the input on whether they want to play or not
        play2 = play.upper() #this line takes the user input and makes it all the letters capital
        if (play2 == 'Y') or (play2 == 'YES'): #this line is checking whether user input is Y or YES
            x = False #this line is to set x to false so that the while loop stops
            return True #this line is to make the function return true if the user types Y or YES
        elif (play2 == 'N') or (play2 == 'NO'): #this line is checking whether user input is N or NO
            x = False #this line is to set x to false so that the while loop stops
            return False #this line is to make the function return false if the user types N or NO
        else:
            print('You must enter Y/YES/N/NO to continue. Please try again') #this line is to tell the user they must enter a valid input
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    y = True #this line sets y to true 
    while y: #this line is to set the while loop to y so that it runs when true
        wager = int(input('How many chips do you want to wager? ==> ')) #this line is asking the user for an integer of how many chips they want to wager
        if wager <= 0: #this line is checking for an input less than or equal to 0 if the input is less than or equal to 0 than it prints the statement and asks for a wager again
            print('The wager must be greater than 0.')
        elif wager > bank: #this line is checking for input greater than the bank if the input is greater than the bank than it prints the statement and asks for a wager again
            print(f'The wager amount cannot be greater than how much you have. {bank}')
        else:
            y = False #this line is to set y to false when a valid input is given so it stops the while loop
    return wager #this return statement is to return the value of wager     

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    a = random.randint(1,10) #this line is to set the a to random integer between 1 to 10
    b = random.randint(1,10) #this line is to set the b to random integer between 1 to 10
    c = random.randint(1,10) #this line is to set the c to random integer between 1 to 10
    return a, b, c #this line outputs the values of a, b, and c

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if (reela == reelb) and (reela == reelc): #this line is to check if all the values are equal and if they are, 3 is returned
        return 3
    elif (reela == reelb) and (reela != reelc): #this is to check if 2 values are equal and if they are, 2 is returned
        return 2
    elif (reela != reelb) and (reelb == reelc): #this is to check if 2 values are equal and if they are, 2 is returned
        return 2
    elif (reela == reelc) and (reelb != reelc): #this is to check if 2 values are equal and if they are, 2 is returned
        return 2
    else:
        return 0 #this line is if none of the values are equal and returns 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    x = True #this line sets x to true
    while x: #this line is to set the while to x so that when x is true, the while loop keeps running
        chips = int(input('How many chips do you want to start with? ==> ')) #this line ask for a user input of how many chips they want and is an integer 
        if chips <= 0: #this line is to check if chips are less than or equal to 0 and if it is the statement is printed and the user is asked again for a valid input
            print('Too low a value, you can only choose 1 - 100 chips')
        elif chips > 100: #this line is to check if chips are greater than 100 and if it is the statement is printed and the user is asked again for a valid input
            print('Too high a value, you can only choose 1 - 100 chips')
        else: 
            x = False #this line is to set x to false and stops the while loop
    return chips #this line returns the value of chips

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3: #this line is to check if matches is equal to 3
        result = (wager * 10) - wager #this line sets the result to wager times 10 and then minus the wager to get a new amount the user can wager
        return result #this line returns the result
    elif matches == 2: #this line is to check if matches is equal to 2
        result = (wager * 3) - wager #this line sets the result to wager times 3 and then minus the wager to get a new amount the user can wager
        return result #this line returns the result
    else:
        return wager * -1 #this line returns the wager as a negative number if the matches is not equal to 3 or 2


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        spin = 0 #this line sets spin to 0

        while True:  #this line sets the while to true so that it runs while true

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spin += 1 #this line adds 1 to spin for everytime it goes through the loop to count the number of spins done
            if bank == 0: #this line is check if bank has reached 0 and when it does it stops the while loop
                break #this line stops the loop
            
        print("You lost all", wager, "in", spin, "spins") #this line is to print the wager you lost in the number of spins
        print("The most chips you had was", bank) #this line is to print the most chips you had in the bank
        playing = play_again() 
