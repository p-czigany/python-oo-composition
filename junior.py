from has_name import HasName
from has_senior import HasSenior


class Junior(HasSenior, HasName):

    def __init__(self, name, senior: HasName):
        HasName.__init__(self, name)
        HasSenior.__init__(self, senior)
