import secrets
from math import log2
from enum import IntEnum, StrEnum
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class Symbols(StrEnum):
    LOWERCASE = ascii_lowercase
    UPPERCASE = ascii_uppercase
    DIGITS = digits
    PUNCTUATION = punctuation
    BAD_SYMBOLS = "liLI"
    CLEAR_LOWERCASE = "abcdefghjkmnopqrstuvwxyz"
    CLEAR_UPPERCASE = "ABCDEFGHJKMNOPQRSTUVWXYZ"


class StrengthToEntropy(IntEnum):
    Empty = 0
    Pathetic = 1
    Weak = 30
    Good = 50
    Strong = 70
    Excellent = 120


def create_new_password(pass_len: int, char: str) -> str:
    return "".join(secrets.choice(char) for _ in range(pass_len))


def get_password_entropy(pass_len: int, char_num: int) -> float:
    return round((pass_len * log2(char_num)), 1)


def delete_bad_symbols(ascii_symbols: str) -> str:
    return ascii_symbols.translate({ord(i): None for i in Symbols.BAD_SYMBOLS})


def delete_symbols(ascii_symbols: str, del_ascii_symbols: str) -> str:
    return ascii_symbols.translate({ord(i): None for i in del_ascii_symbols})
