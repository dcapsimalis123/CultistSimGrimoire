from Word import Word
from uuid import uuid1

class Card(Word):
    # components
        # items
            # uuid
            # name
            # equation list
        # funcs
            # __init__
            # __str__
            # full print
            # new equation check
    def __init__(self, input_name):
        self.uuid = uuid1()
        self.name = input_name 
        self.equation_list = [] # just a list of equation uuid's its a part of
    def print(self,grimoire):
        # This prints out to terminal name, maybe the flavor text, and then the equations
        print(f'Name: {self.name}')
        print(f'uuid: {self.uuid}')
        [grimoire.equation_list(eq) for eq in self.equation_list]