num = int(input("Enter a number: "))

sum = 0
original_num = num

while num != 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10

print('sum is= ', sum)
print('Multiplication is=', prod)

if (original_num % sum) == 0:
    print('niven number')
else:
    print('Not a niven number')