class Employee:

    def __def__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'



emp1 = Employee('Daniel', 'De la Portilla', 3000000)
emp2 = Employee('David', 'Rios', 2000000)

print(emp1)
