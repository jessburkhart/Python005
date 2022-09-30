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
    for i in range(0,9): #this line is go through number 0 through 8
        if (i < 5) and (i >= 0): #this line is to check for numbers between 0 and 5
            num1 = character_value(card[i]) #this line takes the character at index i of the string card, and runs it through the function character_value
            values.append(num1) #this line adds the number to the list values
        if (i >= 5) and (i <= 8): #this line is to check fro numbers between 5 and 8 inclusive
            num2 = character_value(card[i]) #this line takes the character at index i of the string, and runs it through the function character_value
            values.append(num2) #this line adds the number to the list values
    secondvalues = [] #this line is to make an empty list, so numbers can be added to it
    for x in range(0,9): #this line is to go through number 0 through 8
        total = (x + 1) * values[x] #this line takes the number x plus 1 and then multiplied by the value at index x
        secondvalues.append(total) #this line adds the number to the list secondvalues
    secondtotal = 0 #this line assigns secondtotal to 0 
    for y in secondvalues: #this line goes through the elements in the list secondvalues
        secondtotal += y #this line adds y to secondtotal
    final = secondtotal %10 #this line takes secondtotal and gets the remainder when divided by 10
    return final #this line returns the value for final

def verify_check_digit(card):
    if len(card) != 10: #this line is to check if the string card has a length of 10, and if it is not length 10, it returns false
        return (False, 'The length of the number given must be 10') 
    for a in range(0,5): 
        if card[a].isalpha() == False: #this line checks if it is all letters at index a in the string card, and if equal to false, it returns false
            return (False, f'The first 5 characters must be A-Z, the invalid character is at {a} is {card[a]}')
    for b in range(7,10):
        if card[b].isdigit() == False: #this line checks if it is all digits at index b in the string card, and if equal to false, it returns false
            return (False, f'The last 3 characters must be 0-9, the invalid character is at {b} is {card[b]}')
    if (int(card[5]) > 3) or (int(card[5]) < 1): #this line checks to see if the element at index 5 in the string is not between 1 and 3, and if so, it returns false
        return (False, 'The sixth character must be 1 2 or 3')
    if (int(card[6]) > 4) or (int(card[6]) < 1): #this line checks to see if the element at index 6 in the string is not between 1 and 4, and if so, it returns false
        return (False, 'The seventh character must be 1 2 3 or 4')
    if int(card[9]) != (get_check_digit(card)): #this line checks to see if the element at index 9 is not equal to the string when ran through the function get_check_digit, and if not equal, it returns false
        return (False, f'Check digit {card[9]} does not match calculated value {get_check_digit(card)}.')
    else:
        return (True, '') #if it doesn't return false for any, it returns true



if __name__ == "__main__":

    # main program
    print('{:^60}'.format('Linda Hall')) #this line is to center Linda Hall
    print('{:^60}'.format('Library Card Check')) #this line is to center Library Card Check
    print('='*60) #this line is to print 60 equal signs
    print()
    while True: #this line is to run the while loop when true
        lcard = input('Enter Library Card. Hit Enter to Exit ==> ') #this line assigns lcard to the user input
        x, y = verify_check_digit(lcard) #this line assigns x and y to the value returned when lcard is put into the verify_check_digit function
        if len(lcard) != 0: #this line checks to if it is all characters and numbers in lcard
            if x == False: #this line checks to see if x is equal to false, and if so, it prints the statements
                print('Library card is invalid.')
                print(y)
            elif x == True: #this line checks to see if x is equal to true, and if so, it prints the statements
                print('Library card is valid.')
                print(f'The card belongs to a student in {get_school(lcard)}') #this line prints the value when lcard is put through the get_school function
                print(f'The card belongs to a {get_grade(lcard)}') #this line prints the value when lcard is put through the get_grade function
            print()
        if len(lcard) == 0: #this line checks to see if it is all characters and numbers in lcard, and if false, it breaks from the loop
            break
