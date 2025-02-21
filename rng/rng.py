from newline import newline
from random import randint
def rng(list:list):
    result = list[randint(0, len(list)-1)]
    return result
