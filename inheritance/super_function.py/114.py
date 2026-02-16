class Employee:
    def __init__(self, salary):
        self.salary = salary


class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus
