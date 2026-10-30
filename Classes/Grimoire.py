from Globals import ALL_EQUATION_TYPES
from Word import Word
from Equation import Equation
from Operator import Operator
from Card import Card

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

    def load_from_binary(self, save_file : str) -> None:
        pass

    def write_into_binary(self, save_file : str) -> None:
        pass

    def input_eq():
        pass

    def display_word_info():
        pass

    def strip_equation(self,inputed_string) -> Equation:
        split = inputed_string.split(' ')
        equation_temp = []
        new_word_list = []
        for i, word in enumerate(split):
            if split in ALL_EQUATION_TYPES.values():
                next_word = ALL_EQUATION_TYPES[word]
            elif self.new_word_check(split):
                next_word = Word(word)
                new_word_list.append(next_word)
            equation_temp.append(next_word)
        return equation_temp

    def new_word_check(self, new_word : Card) -> bool:
        return new_word not in self.tile_hash_table.values()

    def new_equation_check(self, new_equation : Equation) -> bool:
        try:
            self.equation_list[new_equation.uuid]
            return False
        except:
            print("New Equation Found")
            self.equation_list[new_equation.uuid] = new_equation
            return True