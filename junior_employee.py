from employee import Employee
from junior import Junior


class JuniorEmployee(Junior, Employee):

    def __init__(self, name, senior: Employee):
        Employee.__init__(self, name)
        Junior.__init__(self, senior)
