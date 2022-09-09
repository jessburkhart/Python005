#this line is to welcome the user and be the start of the program
print('**** Welcome to the LAB grade calculator! ****\n')
#this line asks user for their name and assigns input to name
name = input('Who are we calculating grades for? ==> ')
#added print() statement to add a space between lines
print()
#this line asks user for lab grade input and assigns input to labgrade
labgrade = int(input('Enter the Labs grade? ==> '))
#these lines are an if and elif statement to check whether user input values greater than 100 or less than 0, and then corrects it to either 100 or 0
if labgrade < 0:
    labgrade = 0
    print('The lab value should have been zero or greater. It has been changed to zero.')
elif labgrade > 100:
    labgrade = 100
    print('The lab value should have been 100 or less. It has been change to 100.')
#added print() statement to add a space between lines
print()
#this line asks user for exam grade input and assigns input to examgrade
examgrade = int(input('Enter the EXAMS grade? ==> '))
#these lines are an if and elif statement to check whether user input values greater than 100 or less than 0, and then corrects it to either 100 or 0
if examgrade < 0:
    examgrade = 0
    print('The exam value should have been zero or greater. It has been changed to zero.')
elif examgrade > 100:
    examgrade = 100
    print('The exam value should have been 100 or less. It has been change to 100.')
#added print() statement to add a space between lines
print()
#this line asks user for attendance grade input and assigns input to attendance
attendance = int(input('Enter the Attendance grade? ==> '))
#these lines are an if and elif statement to check whether user input values greater than 100 or less than 0, and then corrects it to either 100 or 0
if attendance < 0:
    attendance = 0
    print('The attendance value should have been zero or greater. It has been changed to zero.')
elif attendance > 100:
    attendance = 100
    print('The attendance value should have been 100 or less. It has been change to 100.')
#added print() statement to add a space between lines
print()
#this line is an equation to figure out the weighted grade and assigned it to variable weightgrade
weightgrade = (labgrade * 0.7) + (examgrade * 0.2) + (attendance * 0.1)
#this line outputs user's weighted grade
print(f'The weighted grade for {name} is {weightgrade}')
#these lines are if, elif, and else statements to figure out the letter grade by using the weighted grade, and then outputs the letter grade to the user
if (weightgrade >= 90) and (weightgrade <= 100):
    lettergrade = 'A'
    print(f'{name} has a letter grade of {lettergrade}\n')
elif (weightgrade >= 80) and (weightgrade < 90):
    lettergrade = 'B'
    print(f'{name} has a letter grade of {lettergrade}\n')
elif (weightgrade >= 70) and (weightgrade < 80):
    lettergrade = 'C'
    print(f'{name} has a letter grade of {lettergrade}\n')
elif (weightgrade >= 60) and (weightgrade < 70):
    lettergrade = 'D'
    print(f'{name} has a letter grade of {lettergrade}\n')
else:
    lettergrade = 'F'
    print(f'{name} has a letter grade of {lettergrade}\n')
#this line is to thank the user for using the program and be the end of the program
print('**** Thanks for using the Lab grade calculator ****')
