num = int(input("Enter a number: "))
m = num

sum = 0
while num != 0:
    rem = num % 10

    sum = sum * 10 + rem
    num = num // 10

if sum = m:
    print('palindrome')
else:
    print('not palindrome')