# def add_sum_avg(a, b, c):
#     sum = a + b + c
#     average = sum / 3
#     print(sum)
#     print(average)
#
# add_sum_avg(10, 20, 30)

# def add_sum_avg(a, b, c):
#     sum = a + b + c
#     average = sum / 3
#     return sum, average
#
# print(add_sum_avg(10, 20, 30))

# def find_factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     print(f'factorialis: {fact}')

# class apartment_101:
#     pass
# person1 = apartment_101()
# person2 = apartment_101()
# person3 = apartment_101()
# person4 = apartment_101()
#
# person1.first = 'Alex'
# person1.last = 'Rahu'
# person1.email = 'alex.rahu@company.com'
# person1.salary = 3000
# person1.profession = 'IT-head'
#
# person2.first = 'David'
# person2.last = 'Rebane'
# person2.email = 'david.rebane@company.com'
# person2.salary = 4000
# person2.profession = 'Doctor'
#
# print(person1.salary)
# print(person2.email)

# class apartment_101:
#     def __init__(self, first, last, salary, profession):
#         self.first = first
#         self.last = last
#         self.salary = salary
#         self.profession = profession
#
#     def full_name(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def email_address(self):
#         return '{} {}'.format(self.first, self.last + '@company.com')
#
# person1 = apartment_101('Alex', 'Rahu', 3000, 'IT-Juht')
# person2 = apartment_101('David', 'Rebane', 4000, 'Doctor')
# person3 = apartment_101('Oskar', 'Rahumagi', 2000, 'Chef')
# person4 = apartment_101('Robin', 'Khan', 5000, 'IT')
#
# print(person1.profession)
# print(person2.full_name())
# print(person3.email_address())

class smart_phone:
    def __init__(self, company_name, model, price, condition):
        self.company_name = company_name
        self.model = model
        self.price = price
        self.condition = condition

    def details(self):
        return '{}, {}'.format(self.company_name, self.model + ' 16 Pro Max')

    def high_price(self):
        return self.price * 1.6

phone1 = smart_phone('Apple', 'IPhone', 1699, 'New')
phone2 = smart_phone('Samsung', 's55', 669, 'New')

print(phone1.details())
print(f'{phone1.price}$')