import math #this line imports the math module
tests = [] #this line assigns tests to an empty list
assignments = [] #this line assigns assignments to an empty list


def avg_(list1):
    avgscore = 0 #this line assigns avgscore equal to 0
    try:
        for i in list1: #this line loops through the elements in the list
            avgscore += i #this line adds the elements to the avgscore
        avgscore = avgscore/len(list1) #this line divides the avgscore by the length of the list
    except ZeroDivisionError: #this line checks if you are dividing by zero
        avgscore = 0 #this line sets the avgscore equal to 0
    return avgscore #this line returns the avgscore

def std_(list1):
    mean = avg_(list1) #this line calls the function avg_() with list1 as the argument and assigns it to mean
    total = 0 #this line assigns total to 0
    for i in list1: #this line loops through the elements in the list
        x = pow((i - mean),2) #this line takes the element subtracted by the mean and then squares it and assigns it to x
        total += x #this line adds x to the total
    std = math.sqrt(total/len(list1)) #this line takes the total divided by the length of the list and the takes the square root and assigns it to std
    return std #this line returns std

def weightgrade(tests,assignments):
    t = (avg_(tests)) * 0.6 #this line calls the function avg_() with tests as the argument and then multiplied by 0.6 and assigns it to t
    a = (avg_(assignments)) * 0.4 #this line calls the function avg_() with assignments as the argument and then multiplied by 0.4 and assigns it to a
    final = t + a #this adds t and a together and assigns it to final
    return final #this line returns final

def display():
    if (len(tests) == 0) and (len(assignments) == 0): #this line checks if the length of tests and assigments are both zero and if so it prints the statements
        print('{} {:>15} {:>8} {:>8} {:>8} {:>8}'.format('Type','#','min','max','avg','std'))
        print('='*56)
        print('{} {:>14} {:>8} {:>8} {:>8} {:>8}'.format('Tests',len(tests),'n/a','n/a','n/a','n/a'))
        print('{} {:>11} {:>8} {:>8} {:>8} {:>8}'.format('Programs',len(assignments),'n/a','n/a','n/a','n/a'))
        print()
        print('The weighted score is 0.00')
    elif len(tests) == 0: #this line checks if the length of tests is zero and if so it prints the statements
        print('{} {:>15} {:>8} {:>8} {:>8} {:>8}'.format('Type','#','min','max','avg','std'))
        print('='*56)
        print('{} {:>14} {:>8} {:>8} {:>8} {:>8}'.format('Tests',len(tests),'n/a','n/a','n/a','n/a'))
        print('{} {:>11} {:>8} {:>8} {:>8} {:>8}'.format('Programs',len(assignments),min(assignments),max(assignments),avg_(assignments),round(std_(assignments),2)))
        print()
        print(f'The weighted score is {weightgrade(tests,assignments)}')
    elif len(assignments) == 0: #this line checks if the length of assignments is zero and if so it prints the statements
        print('{} {:>15} {:>8} {:>8} {:>8} {:>8}'.format('Type','#','min','max','avg','std'))
        print('='*56)
        print('{} {:>14} {:>8} {:>8} {:>8} {:>8}'.format('Tests',len(tests),min(tests),max(tests),avg_(tests),round(std_(tests),2)))
        print('{} {:>11} {:>8} {:>8} {:>8} {:>8}'.format('Programs',len(assignments),'n/a','n/a','n/a','n/a'))
        print()
        print(f'The weighted score is {weightgrade(tests,assignments)}')
    else: #this line prints the statements if the length of test and assignments are not equal to zero
        print('{} {:>15} {:>8} {:>8} {:>8} {:>8}'.format('Type','#','min','max','avg','std'))
        print('='*56)
        print('{} {:>14} {:>8} {:>8} {:>8} {:>8}'.format('Tests',len(tests),min(tests),max(tests),avg_(tests),round(std_(tests),2)))
        print('{} {:>11} {:>8} {:>8} {:>8} {:>8}'.format('Programs',len(assignments),min(assignments),max(assignments),avg_(assignments),round(std_(assignments),2)))
        print()
        print('The weighted score is %.2f' %(weightgrade(tests,assignments)))
                

while True: #this line loops while true
    print()
    print('{:^30}'.format('Grade Menu'))
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Quit\n')
    x = input('==> ') #this line prompts the user for an input and assigns it to x
    print()
    if x.upper() == 'Q': #this line checks if x is equal to Q and if so it breaks out of the loop
        break
    elif x.upper() == 'D': #this line checks if x is equal to D and if so it calls the function display()
        display()
    elif x == '1': #this line checks if x is equal to 1
        while True: #this line loops while true
            try:
                newtest = float(input('Enter the new Test score 0-100 ==> ')) #this line prompts the user for a float input and assigns it to newtest
                if newtest < 0: #this line checks to see if newtest is less than 0 and then prints the statement
                    print('Enter a valid Test score')
                else:
                    tests.append(newtest) #this line appends newtest to tests if greater than 0 
                    break #this line breaks out of the loop
            except: #this line checks if the input was not a float and then prints the statement
                print('Enter a valid Test score') 
    elif x == '2': #this line checks if x is equal to 2
        while True:
            try:
                removetest = float(input('Enter the Test score to remove 0-100 ==> ')) #this input prompts the user for a float input and assigns it to removetest
                if removetest < 0: #this line checks if the removetest is less than 0 and then prints the statement
                    print('Enter a valid Test score')
                else:
                    try:
                        tests.remove(removetest) #this line removes removetest from tests and then breaks out of the loop
                        break
                    except:
                        print('Could not find that score to remove') #this line checks if removetest is in tests to remove and if not it prints the statement and breaks out of the loop
                        break
            except: #this line checks if user input was valid and if not if prints statement
                print('Enter a valid Test Score') 
    elif x == '3': #this line checks if x is equal to 3
        tests = [] #this line sets tests back to an empty list
    elif x == '4': #this line checks if x is equal to 4
        while True:
            try:
                newassign = float(input('Enter the new Assignment score 0-100 ==> ')) #this line prompts user for float input and assigns it to newassign
                if newassign < 0: #this line checks if newassign is less than 0 and then prints the statements
                    print('Enter a valid Assignment score')
                else:
                    assignments.append(newassign) #this line appends newassign to assignments and then breaks out of the loop
                    break
            except: #this line checks to see if user input was valid and if not prints the statement
                print('Enter a valid Assignment score')
    elif x == '5': #this line checks if x is equal to 5
        while True:
            try:
                removeassign = float(input('Enter the Assignment score to remove 0-100 ==> ')) #this line prompts the user for a float input and assigns it to removeassign
                if removeassign < 0: #this line checks if removeassign is less than 0 and then prints the statement
                    print('Enter a valid Assignment score')
                else:
                    try:
                        assignments.remove(removeassign) #this line removes removeassign from assignments and then breaks out of the loop
                        break
                    except: #this line checks if removeassign is in assignments to remove and if not it prints the statement and breaks out of the loop
                        print('Could not find that score to remove')
                        break
            except: #this line checks to see if user input was valid and if not prints the statement
                print('Enter a valid Assignment score')
    elif x == '6': #this line checks if x is equal to 6
        assignments = [] #this line sets assignements back to an empty list
    else: #this line checks if user input was a valid input and if not it prints the statement
        print('Enter a valid option')
        

