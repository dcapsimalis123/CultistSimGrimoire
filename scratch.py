import numpy as np
import matplotlib.pyplot as plt
import type_enforced
from uuid import uuid1

ALL_EQUATION_TYPES ={
    "Assignment": '===',
    "Create"    : '==>',
    "Consumed"  : '[:.',
    "Cure"      : '[+]',
    "Dangerous" : '<x>',
    "Decay"     : '/=/',
    "Grab"      : '}=>',
    "Unsure"    : '?_?',
}

class Equation():
    #components
        # items
            # uuid
            # word list [both words and operations are words in this case]
        # funcs
        # init
        # __str__
        # 
    def __init__(self,inputed_strings : list[tuple[int,str]]):
        self.input_words = [] # string names
        self.equation_type = ''
        self.output_words  = [] # string names
        self.uuid = uuid1
        for word in inputed_strings:
            if word.name in ALL_EQUATION_TYPES.keys():
                self.equation_type = word.name
            elif self.equation_type != []:
                self.input_words.append(word.name)
            else:
                self.output_words.append(word.name)
            pass


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


class Grimoire():
    # components
        # items
            # tile_hash_table 
            # equation_list
            # operator list
        # funcs
            # __init__
            # load_from_binary
            # write_into_binary
            # strip equation
            # new word check
            # new equation check
            # 
    def __init__(self):
        # list of tile objects
        self.tile_hashtable = {}          # relates the tiles uuid to the obj
        self.tile_hashtable_reversed = {} # relates the tile obj to their uuid
        # list of equation objects
        self.equation_list = {}           # relates the tiles uuid to obj
        self.equation_list_reveresed = {} # relates the tile obj to their uuid

        self.operator_list = {y : uuid1() for y in ALL_OPERATOR_SYMBOLS}
        self.operator_list_reversed = {v: k for k, v in self.operator_list.items()}
        pass

    def load_from_binary(self, save_file : str) -> None:
        pass

    def write_into_binary(self, save_file : str) -> None:
        pass

    def strip_equation(self,inputed_string) -> Equation:
        splitted = inputed_string.split(' ')
        equation_temp = []
        new_word_list = []
        for i, word in enumerate(splitted):
            if splitted in ALL_OPERATOR_SYMBOLS:
                next_word = self.operator_list[word]
            elif self.new_word_check(splitted):
                next_word = Word(word)
                new_word_list.append(next_word)
            equation_temp.append(next_word)
        return equation_temp

    def new_word_check(self, new_word) -> bool:
        return new_word not in self.tile_hash_table.values()

    def new_equation_check(self, new_word) -> bool:
        pass

