"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryEmp(Employee):
    def __init__ (self, name, amount):
        super().__init__(name)
        self.amount = amount

    def get_pay(self):
        return self.amount

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.amount}.  Their total pay is {self.amount}."

class SalaryBonusEmp(SalaryEmp):
    def __init__ (self, name, amount, bonus):
        super().__init__(name, amount)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.amount} and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}."

class SalaryContractEmp(SalaryEmp):
    def __init__ (self, name, amount, contracts, commission):
        super().__init__(name, amount)
        self.contracts = contracts
        self.commission = commission

    def get_pay(self):
        return super().get_pay() + (self.contracts * self.commission)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.amount} and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."


class HourlyEmp(Employee):
    def __init__ (self, name, wage, hours):
        super().__init__(name)
        self.wage = wage
        self.hours = hours

    def get_pay(self):
        return self.wage * self.hours

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour.  Their total pay is {self.get_pay()}."


class HourlyBonusEmp(HourlyEmp):
    def __init__ (self, name, wage, hours, bonus):
        super().__init__(name, wage, hours)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}."

class HourlyContractEmp(HourlyEmp):
    def __init__ (self, name, wage, hours, contracts, commission):
        super().__init__(name, wage, hours)
        self.contracts = contracts
        self.commission = commission

    def get_pay(self):
        return super().get_pay() + (self.contracts * self.commission)

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmp('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmp('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryContractEmp('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContractEmp('Jan', 25, 150, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryBonusEmp('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyBonusEmp('Ariel', 30, 120, 600)
