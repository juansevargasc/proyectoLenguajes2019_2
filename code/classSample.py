class Employee:
    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)


emp1 = Employee('Daniel', 'De la Portilla', 300)
emp1.raise_amount = 1.10

emp2 = Employee('David', 'Rios', 200)

print(emp1.email) #de la Portilla
print(emp1.fullname())
print(Employee.fullname(emp2))

print('One moment please, loading information')

print('Employees Standard: ', Employee.raise_amount)
print(emp1.raise_amount)
print('Emp2 ', )



# #define yywrap() 1
#undef yywrap
