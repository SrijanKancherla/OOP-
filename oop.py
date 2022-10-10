#Python Object-Oriented Programming

class Employee: # class name should be in CamelCase and this is a convention

    num_of_emps = 0
    raise_amt = 1.04 # this is a class variable
    
    def __init__(self, first, last, pay): # this is a constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str.lower(first + '.' + last + '@company.com')

        Employee.num_of_emps += 1
        
    def fullname(self): # this is a method
        return '{} {}'.format(self.first, self.last) 

    def apply_raise(self): # this is a method
        self.pay = int(self.pay * self.raise_amt) 
    
    @classmethod # this is a decorator
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    @staticmethod 
    def what_day(day):
        its_a = day.strftime('%A') # %A is a format code for day of the week, using strftime is easier
        return "It's a " + its_a
        # if day.weekday() == 0:
        #     return 'Monday'
        # elif day.weekday() == 1:
        #     return 'Tuesday'
        # elif day.weekday() == 2:
        #     return 'Wednesday'
        # elif day.weekday() == 3:
        #     return 'Thursday'
        # elif day.weekday() == 4:
        #     return 'Friday'
        # elif day.weekday() == 5:
        #     return 'Saturday'
        # elif day.weekday() == 6:
        #     return 'Sunday'
        # else:
        #     return 'Not a day'
        
emp_1 = Employee('Srijan', 'Karthik', 50000) # this is an instance of the class Employee
emp_2 = Employee('Test', 'User', 60000) # this is another instance of the class Employee

import datetime
my_date = datetime.date(2022, 10, 8)
print(Employee.is_workday(my_date))
print(Employee.what_day(my_date))

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)







# print(emp_1.__dict__) # this is a dictionary of the instance emp_1
# print(Employee.__dict__) # this is a dictionary of the class Employee 

# print(emp_1, emp_2)

# emp_1.first = 'Srijan'
# emp_1.last = 'Karthik'
# emp_1.email = 'srijan.karthik@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'test.user@company.com'
# emp_2.pay = 60000 

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname()) # this is the same as Employee.fullname(emp_1), and how you should do it
# print(Employee.fullname(emp_1)) #what is actually going on in the background




