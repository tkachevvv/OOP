def is_neon_number(num):
    return sum(int(digit) for digit in str(num**2)) == num

number = 9
print(f"{number} neon" if is_neon_number(number) else f"{number} not neon")
