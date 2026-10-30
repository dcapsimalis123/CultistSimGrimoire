import numpy as np
import matplotlib.pyplot as plt
from uuid import uuid1
from Classes.Card import Card
from Classes.Equation import Equation
from Classes.Grimoire import Grimoire
from Classes.Word import Word
from Globals import ALL_EQUATION_TYPES

if __name__ == "__main__":
    main_tome = Grimoire()
    main_tome.load_from_binary()