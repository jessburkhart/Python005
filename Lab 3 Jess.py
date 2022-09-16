#this line is to welcome the user to the game
print('Welcome to the Flarsheim Guesser!')
#this line is to set play to true so that the while loop runs while play is true
play = True
while play:
    print() 
    print('Please think of a number between and including 1 and 100.\n') #this line is to tell the user to think of number to play
    x = True #this line is to set x to true so the nested while loop runs until it gets a valid input from the user and then x is set to false to exit the loop
    while x:
        num1 = int(input('What is the remainder when your number is divided by 3 ?'))
        if num1 < 0: #this line is to check for a valid input from the user because the input cannot be less than 0
            print('The value entered must be 0 or greater')
        elif num1 >= 3: #this line is to check for a valid input from the user because the input cannot be greater than or equal to 3
            print('The value entered must be less than 3')
        else: 
            x = False #this line sets x to false to exit the loop if the user gave a valid input
            print()
    y = True #this line is to set y to true so the nested while loop runs until it gets a valid input from the user and then y is set to false to exit the loop
    while y:
        num2 = int(input('What is the remainder when your number is divided by 5 ?'))
        if num2 < 0: #this line is to check for a valid input from the user because the input cannot be less than 0
            print('The value entered must be 0 or greater')
        elif num2 >= 5: #this line is to check for a valid input from the user because the input cannot be greater than or equal to 5
            print('The value entered must be less than 5')
        else:
            y = False #this line sets y to false to exit the loop if the user gave a valid input
            print()
    z = True #this line is to set z to true so the nested while loop runs until it gets a valid input from the user and then z is set to false to exit the loop
    while z:
        num3 = int(input('What is the remainder when your number is divided by 7 ?'))
        if num3 < 0: #this line is to check for a valid input from the user because the input cannot be less than 0
            print('The value entered must be 0 or greater')
        elif num3 >= 7: #this line is to check for a valid input from the user because the input cannot be greater than or equal to 7
            print('The value entered must be less than 7')
        else:
            z = False #this line sets z to false to exit the loop if the user gave a valid input
    for num in range(1,101): #this line is to check for the number in the range 1 to 101, 101 was chosen so the range would include 100 because if 100 was put in the range it would stop at 99
        if (num %3 == num1) and (num %5 == num2) and (num %7 == num3): #this line is to check if the number in the range divided by 3, divided by 5, and divided by 7 equal the remainders the user input
            print(f'Your number was {num}') #this line is to print the number that fits the if statement
            print('How amazing is that?\n')
            a = True #this line sets a to true so that the while loop runs until a returns false
            while a: 
                user_input = input('Do you want to play again? Y to continue, N to quit ==> ') #this line asks the user whether they want to play again and sets the input to user_input
                if (user_input == 'Y') or (user_input == 'y'): #this line checks the user input for Y and y and if they input Y or y then play is set equal to true and runs the game again
                    play = True #this line keeps play equal to true so that the game starts again
                    a = False #this line is to set a to false so that it stops the loop
                elif (user_input == 'N') or (user_input == 'n'): #this line checks the user input for N and n and if they input N or n then play is set equal to false and stops the game
                    play = False #this line sets play equal to false so that the game stops
                    break #this line breaks out of this while loop





    
