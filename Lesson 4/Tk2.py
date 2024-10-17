a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))

while b > 0:
    rem = a % b
    a = b
    b = rem

gcd = a
lcm = (c * m) / gcd
print('gcd is: ', gcd)
print('LCM is ', lcm)