class Employee(object):

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Adam', 'Hamilton', 'xxxx')

#option #1 
#print(emp_1.fullname())

#option #2
print(Employee.fullname(emp_1))