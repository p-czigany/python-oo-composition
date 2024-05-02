class Employee(object):

    def __init__(self, name: str):
        if name is None:
            raise ValueError('\"None\" is not a name, for Pete\'s sake!')
        self.__name = name

    def name(self) -> str:
        return self.__name
