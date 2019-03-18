from shiftchar import shift_str


class WrongKey(Exception):
    pass


def check_key(s):
    try:
        int(s)
    except ValueError:
        raise WrongKey


def action(act: str, s: str, key):
    check_key(key)
    key = int(key)
    if act == "encode":
        return shift_str(s, key)
    else:
        return shift_str(s, key, reverse=True)
