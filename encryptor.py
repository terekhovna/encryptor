#!/usr/bin/python3
# -*- coding: utf-8 -*-
from myparser import init_parse, parsers
import vigenere, caesar
from hacker import hack, train
import pickle

args = init_parse()
if args.action in ["encode", "decode"]:
    cipher = globals()[args.cipher]
    parser = parsers[args.action]
    try:
        result = cipher.action(args.action, args.input.read(), args.key)
        args.output.write(result)
    except cipher.WrongKey:
        parser.error("Некорректный ключ!!!")
    finally:
        args.input.close()
        args.output.close()
elif args.action == "train":
    try:
        data = dict(train(args.text.read()).items())
        pickle.dump(data, args.model)
    finally:
        args.text.close()
        args.model.close()
elif args.action == "hack":
    try:
        args.output.write(hack(args.input.read(), pickle.load(args.model)))
    finally:
        args.input.close()
        args.output.close()
        args.model.close()
else:
    parsers["main"].error("Нет такого действия")

