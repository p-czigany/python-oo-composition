from has_name import HasName
from has_senior import HasSenior
from has_serf import HasSerf


class Senior(HasSenior, HasSerf, HasName):

    def __init__(self, name, senior: HasName, serf: HasName):
        HasSerf.__init__(self, serf)
        HasSenior.__init__(self, senior)
        HasName.__init__(self, name)
