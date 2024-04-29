from has_name import HasName


class HasSerf(object):

    def __init__(self, serf: HasName):
        if serf is None or not isinstance(serf, HasName):
            raise ValueError('A serf should exist and have a name!')
        self.__serf = serf

    def who_is_your_serf(self):
        return self.__serf
