class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay, company="Company"):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str.lower(first + '.' + last + '@{}.com'.format(company))
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang, company="Company"):
        super().__init__(first, last, pay, company)
        # Employee.__init__(self, first, last, pay) # this is another way to do the same thing
        self.prog_lang = prog_lang
        self.email = str.lower(first + '.' + last + '@dev.{}.com'.format(company))
       
class Manager(Employee):
    raise_amt = 1.20
    def __init__(self, first, last, pay, employees=None, company="Company"):
        super().__init__ (first, last, pay, company)
        self.email = str.lower(first + '.' + last + '@manager.{}.com'.format(company))
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
        def add_emp(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)
        
        def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)
        
        def print_emps(self):
            for emp in self.employees:
                print('-->', emp.fullname())

dev_1 = Developer('Srijan', 'Karthik', 50000, 'Python', 'Google')
dev_2 = Developer('Test', 'User', 60000, 'Java', 'Facebook')
mgr_1 = Manager('Vidhya', 'K', 90000, [dev_1], 'Google')

print(isinstance(mgr_1, Manager)) # True
print(isinstance(mgr_1, Employee)) # True
print(isinstance(mgr_1, Developer)) # False
print(issubclass(Developer, Employee)) # True
print(issubclass(Manager, Employee)) # True
print(issubclass(Manager, Developer)) # False


