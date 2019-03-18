from shiftchar import shift_str_use_str


class WrongKey(Exception):
    pass


def check_key(s: str):
    if not s.isalpha():
        raise WrongKey


def action(act: str, s: str, key):
    check_key(key)
    if act == "encode":
        return shift_str_use_str(s, key)
    else:
        return shift_str_use_str(s, key, reverse=True)
