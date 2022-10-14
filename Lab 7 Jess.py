while True:
    try:
        mpg = float(input('Enter the minimum mpg ==> '))
        if mpg <= 0:
            print('Fuel economy given must be greater than 0')
        elif mpg > 100:
            print('Fuel economy must be less than 100')
        else:
            break
    except ValueError:
        print('You must enter a number for the fuel economy')
print()
while True:
    try:
        my_file = input('Enter the name of the input vehicle file ==> ')
        in_file = open(my_file)
        contents = in_file.readlines()
        in_file.close()
        break
    except FileNotFoundError:
        print(f'Could not open file {my_file}')
print()        
while True:
    try:
        my_file2 = input('Enter the name of the file to output to ==> ')
        out_file = open(my_file2, 'w')
        break
    except IOError:
        print(f'There is an IO Error {my_file2}')
print()

for row in contents[1:]:
    car = row.split('\t')
    try:
        if float(car[7]) >= mpg:
            for i in range(len(car)):
                if i >= 0 and i < 3:
                    out_file.write(car[i])
                if i == 7:
                    out_file.write(car[i])
                    out_file.write('\n')
    except ValueError:
        print(f'Could not convert value {car[7]} for {car[0]} {car[1]} {car[2]}')

out_file.close()
                
    
