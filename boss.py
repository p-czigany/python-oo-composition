from employee import Employee
from senior import Senior


class Boss(Employee, Senior):

    def __init__(self, name, serf: Employee):
        Employee.__init__(self, name)
        Senior.__init__(self, serf)
