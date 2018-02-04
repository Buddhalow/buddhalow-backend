from random import choice
from string import ascii_lowercase
n = 10


def generate_id(n=6):
    return "".join(choice(ascii_lowercase) for i in range(n))