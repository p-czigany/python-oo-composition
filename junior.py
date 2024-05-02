from employee import Employee


class Junior(object):
    def __init__(self, senior):
        if senior is None or not isinstance(senior, Employee):
            raise ValueError('A Junior must have a senior who is an Employee!')
        self.__senior = senior

    def daddy(self) -> Employee:
        return self.__senior
