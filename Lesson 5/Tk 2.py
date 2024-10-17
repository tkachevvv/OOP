num = int(input("Enter a number: "))

sum = 0
prod = 1

while num != 0:
    rem = num % 10
    sum = sum + rem
    prod = prod * rem
    num = num // 10

print('sum is= ', sum)
print('Multiplication is=', prod)

if sum == prod:
    print('spy number')
else:
    print('Not a spy number')