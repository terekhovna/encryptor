from shiftchar import get_max_module, get_alphabet_name
from collections import defaultdict


class MyMeta(type):
    def __call__(cls):
        return defaultdict(lambda: defaultdict(float))


class MyModel(metaclass=MyMeta):
    pass


def train(s: str) -> MyModel:
    rez = MyModel()
    count = defaultdict(int)
    for c in s:
        name = get_alphabet_name(c)
        count[name] += 1
        rez[name][c.lower()] += 1
    for name, alphabet in rez.items():
        for c, amount in alphabet.items():
            alphabet[c] = alphabet[c] / count[name] * 100
        rez[name] = alphabet
    return rez


def calc(s: str, model: MyModel) -> float:
    tec = train(s)
    result_delta = 0
    keys = tec.keys() | model.keys()
    for name in keys:
        delta = 0
        a = tec[name]
        b = model[name]
        for c in a.keys() | b.keys():
            delta += (a[c] - b[c]) ** 2
        result_delta += delta ** (1 / len(keys))
    return result_delta


def hack(s: str, model_raw: MyModel) -> str:
    model = MyModel()
    model.update(model_raw)
    import caesar
    minimal = None
    move = 0
    for i in range(get_max_module(s)):
        current = calc(caesar.action("decode", s, i), model)
        if minimal is None or current < minimal:
            minimal = current
            move = i
    return caesar.action("decode", s, move)
