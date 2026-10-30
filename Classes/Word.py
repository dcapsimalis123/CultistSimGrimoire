from uuid import uuid1

class Word():
    # components
        # items
            # uuid
            # name 
        # funcs
            # __init__
            # __str__
    def __init__(self):
        self.uuid = uuid1()
        self.name = ''
    def __str__(self):
        return self.name