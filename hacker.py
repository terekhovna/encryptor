from shiftchar import get_lcm_of_modules, get_alphabet_name
from shiftchar import shift_char, shift_str
from collections import defaultdict


class MyModel(defaultdict):
    def __new__(cls):
        return defaultdict(lambda: defaultdict(int))


def train(s: str) -> MyModel:
    rez = MyModel()
    count = defaultdict(int)

    from collections import Counter
    for c, amount in Counter((c.lower() for c in s)).items():
        rez[get_alphabet_name(c)][c] = amount

    for name in rez.keys():
        count[name] = sum(rez[name].values())

    for name, alphabet in rez.items():
        for c in alphabet:
            alphabet[c] = alphabet[c] / count[name]
    return rez


def calculate_delta(first: MyModel, second: MyModel, shift: int) -> float:
    result_delta = 0
    alphabets = first.keys() | second.keys()

    for name in alphabets:
        delta = 0
        a = first[name]
        b = second[name]
        for c in a.keys() | {shift_char(c, shift, reverse=True) for c in b.keys()}:
            delta += (a[c] - b[shift_char(c, shift)]) ** 2
        result_delta += delta ** (1 / len(alphabets))

    return result_delta


def hack(s: str, model_raw: dict) -> str:
    model = MyModel()
    model.update(model_raw)    
    cur_model = train(s)

    move = 0
    minimal = calculate_delta(model, cur_model, 0)
    
    for i in range(1, get_lcm_of_modules(s)):
        current = calculate_delta(model, cur_model, i)
        if current < minimal:
            move = i
            minimal = current

    return shift_str(s, move, reverse=True)
