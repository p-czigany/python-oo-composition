from employee import Employee


class Senior(object):

    def __init__(self, serf: Employee):
        if serf is None or not isinstance(serf, Employee):
            raise ValueError('A serf should exist and have a name!')
        self.__serf = serf

    def who_is_your_serf(self):
        return self.__serf
