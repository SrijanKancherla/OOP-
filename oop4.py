class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = str.lower(first + '.' + last + '@company.com')
    
    @property
    def email(self):
        return str.lower('{}.{}@email.com'.format(self.first, self.last))

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Successfully deleted employee '{}'".format(self.fullname))
        self.first = None
        self.last = None

emp_1 = Employee('Kaushik', 'R')

emp_1.first = 'Jim'

emp_1.fullname = 'Srijan Karthik'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname) 

del emp_1.fullname