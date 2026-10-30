from uuid import uuid1
from Word import Word
from Globals import ALL_EQUATION_TYPES

class Operator:
    # components
        # items
            # uuid
            # name
            # symbol
        # funcs
            # __init__
            # __str__
    def __init__(self,input_name):
        self.uuid = uuid1()
        self.name = input_name
        self.symbol = ALL_EQUATION_TYPES[input_name]