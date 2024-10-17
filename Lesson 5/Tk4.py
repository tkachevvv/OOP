num = int(input("Enter a number: "))

count =

while num != 0:
    rem = num % 10
    if rem == 0:
        count += 1
    num = num // 10

if count > 0:
    print('duck number')
else:
    print('Not a duck number')
