import string
alphabets = {
    "latin": string.ascii_lowercase,
    "russian": "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "symbol": "".join(chr(i) for i in range(32, 65)),
    None : ""
}


def get_alphabet_name(c: str) -> str:
    if c.isupper():
        return get_alphabet_name(c.lower())
    for name, alphabet in alphabets.items():
        if c in alphabet:
            return name


def get_alphabet(c: str) -> str:
    if c.isupper():
        return get_alphabet(c.lower()).upper()
    return alphabets[get_alphabet_name(c)]


def get_index(c: str) -> int:
    return get_alphabet(c).index(c)


def get_char_modulo(s: str, index: int) -> str:
    mod = len(s)
    return s[(index % mod + mod) % mod]


def size_alphabet(c: str) -> int:
    return len(get_alphabet(c))


def get_lcm_of_modules(s: str) -> int:
    def lcm(a = 0, *args):
        if not args:
            return a
        b = args[0]
        if a == 0 or b == 0:
            lcm_a_b = a or b
        else:
            m = a * b
            while a:
                b %= a
                a, b = b, a
            lcm_a_b = m // b
        return lcm(lcm_a_b, *args[1:])
    return lcm(*{size_alphabet(c) for c in s})


def shift_char(c: str, key: int, reverse: bool = False) -> str:
    if not get_alphabet(c):
        return c
    if reverse:
        key *= -1
    return get_char_modulo(get_alphabet(c), get_index(c) + key)


def shift_str(s: str, key: int, reverse: bool = False) -> str:
    return "".join(map(lambda c: shift_char(c, key, reverse), s))


def shift_str_use_str(s: str, key: str, reverse: bool = False) -> str:
    res = []
    for index, c in enumerate(s):
        shift = get_index(get_char_modulo(key, index))
        res.append(shift_char(c, shift, reverse))
    return "".join(res)
