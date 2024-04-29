from has_name import HasName
from has_serf import HasSerf


class Boss(HasName, HasSerf):

    def __init__(self, name, serf: HasName):
        HasName.__init__(self, name)
        HasSerf.__init__(self, serf)
