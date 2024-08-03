import secrets
from math import log2
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

LOWERCASE = ascii_lowercase
UPPERCASE = ascii_uppercase
DIGITS = digits
PUNCTUATION = punctuation
BAD_SYMBOLS = "liLI"


def create_new_password(pass_len: int, char: str) -> str:
    return "".join(secrets.choice(char) for _ in range(pass_len))


def get_password_entropy(pass_len: int, char_num: str) -> float:
    return round((pass_len * log2(char_num)), 1)


def delete_bad_symbols(ascii_symbols: str) -> str:
    return ascii_symbols.translate({ord(i): None for i in BAD_SYMBOLS})
