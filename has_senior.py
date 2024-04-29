from has_name import HasName


class HasSenior(object):
    def __init__(self, senior):
        if senior is None or not isinstance(senior, HasName):
            raise ValueError('A Junior must have a senior who is an Employee!')
        self.__senior = senior

    def who_is_your_daddy(self) -> HasName:
        return self.__senior
