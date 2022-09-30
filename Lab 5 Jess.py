########################################################################
##
## CS 101 Lab
## Program #5
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


# import statements

# functions
def get_school(card):
    #these lines of code are checking to see if the character at index 5 in the string card is equal to 1, 2, or 3, and  if true, it outputs the school associated with each number
    if int(card[5]) == 1:
        return 'School of Computing and Engineering SCE'
    elif int(card[5]) == 2:
        return 'School of Law'
    elif int(card[5]) == 3:
        return 'College of Arts and Sciences'
    elif (int(card[5]) > 3) and (int(card[5]) <= 0): #this line of code is to check if the character at index 5 in the string is greater than 3 and less than or equal to 0, and if true, it returns invalid school
        return 'Invalid School'

def get_grade(card):
    #these lines of code are checking to see if the character at index 6 in the string card is equal to 1, 2, 3, or 4, and if true, it outputs the grade associated with each number
    if int(card[6]) == 1:
        return 'Freshman'
    elif int(card[6]) == 2:
        return 'Sophomore'
    elif int(card[6]) == 3:
        return 'Junior'
    elif int(card[6]) == 4:
        return 'Senior'
    elif (int(card[6]) > 4) and (int(card[6]) <= 0): #this line of code is to check if the character at index 6 in the string is greater than 4 and less than or equal to 0, and if true, it returns invalid grade
        return 'Invalid Grade'

def character_value(char):
    upperchar = char.upper() #this line of code is to turn the character into an uppercase letter
    num = ord(upperchar) - 65 #this line of code is to get the value of the character by converting the character to an integer and then subtracting 65
    return num #this line returns the num
        
def get_check_digit(card):
    values = [] #this line is to make an empty list, so numbers can be added to it
    for i in range(0,9):
        if (i < 5) and (i >= 0):
            num1 = character_value(card[i])
            values.append(num1)
        if (i >= 5) and (i <= 8):
            num2 = character_value(card[i])
            values.append(num2)
    secondvalues = [] #this line is to make an empty list, so numbers can be added to it
    for x in range(0,9):
        total = (x + 1) * values[x]
        secondvalues.append(total)
    secondtotal = 0
    for y in secondvalues:
        secondtotal += y
    final = secondtotal %10
    return final

def verify_check_digit(card):
    if len(card) != 10:
        return (False, 'The length of the number given must be 10')
    for a in range(0,5):
        if card[a].isalpha() == False:
            return (False, f'The first 5 characters must be A-Z, the invalid character is at {a} is {card[a]}')
    for b in range(7,10):
        if card[b].isdigit() == False:
            return (False, f'The last 3 characters must be 0-9, the invalid character is at {b} is {card[b]}')
    if (int(card[5]) > 3) and (int(card[5]) < 1):
        return (False, 'The sixth character must be 1 2 or 3')
    if (int(card[6]) > 4) and (int(card[6]) < 1):
        return (False, 'The seventh character must be 1 2 3 or 4')
    if int(card[9]) != (get_check_digit(card)):
        return (False, f'Check digit {card[9]} does not match calculated value {get_check_digit(card)}.')
    else:
        return (True, '')



if __name__ == "__main__":

    # main program
    print('{:^60}'.format('Linda Hall'))
    print('{:^60}'.format('Library Card Check'))
    print('='*60)
    print()
    while True:
        lcard = input('Enter Library Card. Hit Enter to Exit ==> ')
        x, y = verify_check_digit(lcard)
        if lcard.isalnum() == True:
            if x == False:
                print('Library card is invalid.')
                print(y)
            elif x == True:
                print('Library card is valid.')
                print(f'The card belongs to a student in {get_school(lcard)}')
                print(f'The card belongs to a {get_grade(lcard)}')
            print()
        if lcard.isalnum() == False:
            break
        
        
        
        
        
