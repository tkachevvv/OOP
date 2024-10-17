to = int(input('Use 1 for C-F, 2 for F-C: '))
value = int(input('Enter the value to convert: '))

match to:
    case 1:
        degrees = (9/5) * value + 32
        print(f'{value}C in Fahrenheit is {degrees} degrees')
    case 2:
        degrees = ((value) - 32) * 5/9
        print(f'{value}F in Celsius is {degrees} degrees')
    case __:
        print('Something went wrong')