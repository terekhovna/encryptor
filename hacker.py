from shiftchar import get_lcm_of_modules, get_alphabet_name
from shiftchar import shift_char, shift_str
from collections import defaultdict


class MyModel(defaultdict):
    def __init__(self):
        super().__init__(lambda: defaultdict(int))
    
    @classmethod
    def from_dict(cls, model_raw: dict):
        model = cls()
        model.update(model_raw)
        return model

    @classmethod
    def train(cls, s: str):
        rez = cls()
        count = defaultdict(int)

        from collections import Counter
        for c, amount in Counter(c.lower() for c in s).items():
            rez[get_alphabet_name(c)][c] = amount

        for name in rez.keys():
            count[name] = sum(rez[name].values())

        for name, alphabet in rez.items():
            for c in alphabet:
                alphabet[c] = alphabet[c] / count[name]

        return rez
    
    def calculate_delta(self, other, shift: int = 0) -> float:
        """сдвигаю self на shift и сравниваю с other"""
        result_delta = 0
        alphabets = self.keys() | other.keys()

        for name in alphabets:
            delta = 0
            a = self[name]
            b = other[name]
            for c in {shift_char(c, shift, reverse=True) for c in a.keys()} | b.keys():
                delta += (b[c] - a[shift_char(c, shift)]) ** 2
            result_delta += delta ** (1 / len(alphabets))

        return result_delta

    @classmethod
    def hack(cls, s: str, model_raw: dict) -> str:
        model = cls.from_dict(model_raw)    
        cur_model = cls.train(s)

        move = 0
        minimal = cur_model.calculate_delta(model)
        
        for i in range(1, get_lcm_of_modules(s)):
            current = cur_model.calculate_delta(model, i)
            if current < minimal:
                move = i
                minimal = current

        return shift_str(s, move, reverse=True)
