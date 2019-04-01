from shiftchar import get_lcm_of_modules, get_alphabet_name
from shiftchar import shift_char, shift_str
from collections import defaultdict


class MyModel(defaultdict):
    def __new__(cls):
        return defaultdict(lambda: defaultdict(int))


def train(s: str) -> MyModel:
    rez = MyModel()
    count = defaultdict(int)
    for c in s:
        name = get_alphabet_name(c)
        count[name] += 1
        rez[name][c.lower()] += 1
    for name, alphabet in rez.items():
        for c in alphabet:
            alphabet[c] = alphabet[c] / count[name]
    return rez


def calculate_delta(first: MyModel, second: MyModel) -> float:
    result_delta = 0
    keys = first.keys() | second.keys()
    for name in keys:
        delta = 0
        a = first[name]
        b = second[name]
        for c in a.keys() | b.keys():
            delta += (a[c] - b[c]) ** 2
        result_delta += delta ** (1 / len(keys))
    return result_delta


def shift_model(model: MyModel) -> MyModel:
    for name, alphabet in model.items():
        model[name] = defaultdict(int)
        model[name].update(
            {shift_char(c, 1, reverse=True): count 
            for c, count in alphabet.items()})
    return model


def hack(s: str, model_raw: dict) -> str:
    model = MyModel()
    model.update(model_raw)    
    cur_model = train(s)

    move = 0
    minimal = calculate_delta(cur_model, model)
    for i in range(1, get_lcm_of_modules(s)):
        shift_model(cur_model)
        current = calculate_delta(cur_model, model)
        if current < minimal:
            move = i
            minimal = current

    return shift_str(s, move, reverse=True)
