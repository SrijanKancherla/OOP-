class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str.lower(first + '.' + last + '@company.com')

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Srijan', 'Karthik', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(repr(emp_1)) #repr is supposed to be for developers, prints code
# print(str(emp_1))  #str is for the user, consumer friendly output

# print(1+2) #basic adding
# print(int.__add__(1, 2)) #this is what the computer is doing

# print('a' + 'b') #string concatenation
# print(str.__add__('a', 'b')) #what the computer is actually doing

# print(len('test')) #length of the string using the len method
# print('test'.__len__()) #what the computer is actually doing

