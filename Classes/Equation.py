from uuid import uuid1
from Globals import ALL_EQUATION_TYPES

class Equation():
    #components
        # items
            # uuid
            # input word list
            # equation type
            # output word list
        # funcs
            # __init__
            # __str__
            # 
    def __init__(self,inputed_strings : list[tuple[int,str]]):
        self.input_words   = [] # string names
        self.equation_type = ''
        self.output_words  = [] # string names
        self.uuid = ''
        for word in inputed_strings:
            if word.name in ALL_EQUATION_TYPES.keys():
                self.equation_type = word.name
            elif self.equation_type != []:
                self.input_words.append(word.name)
            else:
                self.output_words.append(word.name)

        self.uuid += ''.join(self.input_words)
        self.uuid += self.equation_type
        self.uuid += ''.join(self.output_words)