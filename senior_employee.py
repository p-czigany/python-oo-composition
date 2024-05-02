from employee import Employee
from junior import Junior
from senior import Senior


class SeniorEmployee(Junior, Senior, Employee):

    def __init__(self, name, senior: Employee, serf: Employee):
        Senior.__init__(self, serf)
        Junior.__init__(self, senior)
        Employee.__init__(self, name)
