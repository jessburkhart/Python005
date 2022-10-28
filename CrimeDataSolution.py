#imports
import csv


# functions
def month_from_number(num):
    months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    if num >= 1 and num <= 12:
        return months[num]

def read_in_file(filename):
    open_file = open(filename)
    contents = csv.reader(open_file)
    my_list = []
    for line in contents:
        my_list.append([line[1], line[7], line[13]])
    open_file.close()
    return my_list

def create_reported_date_dict(lst):
    my_dict = {}
    for element in lst[1:]:
        if element[0] in my_dict:
            my_dict[element[0]] += 1
        else:
            my_dict[element[0]] = 1
    return my_dict

def create_reported_month_dict(lst):
    my_dict = {}
    for element in lst[1:]:
        if element[0][0] in my_dict:
            my_dict[element[0][0]] += 1
        else:
            my_dict[element[0][0]] = 1
    return my_dict

def create_offense_dict(lst):
    my_dict = {}
    for element in lst[1:]:
        if element[1] in my_dict:
            my_dict[element[1]] += 1
        else:
            my_dict[element[1]] = 1
    return my_dict

def create_offense_by_zip(lst):
    newdict = create_offense_dict(lst)
    my_dict2 = {}
    for k in newdict.keys():
        my_dict = {}
        for element in lst[1:]:
            if element[1] == k:
                if element[2] in my_dict:
                    my_dict[element[2]] += 1
                else:
                    my_dict[element[2]] = 1
        my_dict2[k] = my_dict
    return my_dict2
           


if __name__ == "__main__":

    # Main program
    print("KCPD Crime Data")
    while True:
        try:
            filename = input('Enter the name of the crime data file ==> ')
            my_file = read_in_file(filename)
            break
        except:
            print(f'Could not find the file specified. {my_file} not found')
    print()
    months = create_reported_month_dict(my_file)
    for k,v in months.items():
        if months[k] == max(months.values()):
            mon = k
            maxm = months[k]
    himonth = month_from_number(int(mon))
    print(f'The month with the highest # of crime is {himonth} with {maxm} offenses')
    off = create_offense_dict(my_file)
    for x,y in off.items():
        if off[x] == max(off.values()):
            crime = x
            maxim = off[x]
    print(f'The offense with the highest # of crimes is {crime} with {maxim} offenses')
    print()
    while True:
        offense = input('Enter an offense ==> ')
        offensedict = create_offense_dict(my_file)
        if offense not in offensedict:
            print('Not a valid offense found, please try again')
        else:
            break
    print()
    print(f'{offense} offenses by Zip Code')
    print('{} {:>21}'.format('Zip Code', '# Offenses'))
    print('='*30)
    zipcode = create_offense_by_zip(my_file)
    for k,v in zipcode.items():
        for x,y in v.items():
            if k == offense:
                print('{} {:>24}'.format(x,y))
        

