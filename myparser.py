import argparse
import sys

parsers = {}


def add_cipher(parser):
    parser.add_argument("--cipher", metavar="Шифр", choices=["caesar", "vigenere"],
                        help="тип шифра", required=True)
    parser.add_argument("--key", metavar="Ключ", help="Ключ для Шифра", required=True)


def add_files(parser):
    parser.add_argument("--input-file", dest="input", metavar="Входной файл",
                        type=argparse.FileType('r', encoding="utf-8"), default=sys.stdin)
    parser.add_argument("--output-file", dest="output", metavar="Выходной файл",
                        type=argparse.FileType('w', encoding="utf-8"), default=sys.stdout)


def add_text_file(parser):
    parser.add_argument("--text-file", dest="text", metavar="Входной файл для обучения",
                        type=argparse.FileType('r', encoding="utf-8"), default=sys.stdin)


def add_model_file(parser, c):
    parser.add_argument("--model-file", dest="model", metavar="Файл модели",
                        type=argparse.FileType(c), required=True)


def add_encode(subparsers):
    parsers["encode"] = subparsers.add_parser("encode", help="Закодировать")
    parser = parsers["encode"]
    add_cipher(parser)
    add_files(parser)


def add_decode(subparsers):
    parsers["decode"] = subparsers.add_parser("decode", help="Раскодировать")
    parser = parsers["decode"]
    add_cipher(parser)
    add_files(parser)


def add_train(subparsers):
    parsers["train"] = subparsers.add_parser("train", help="Обучить для взлома")
    parser = parsers["train"]
    add_text_file(parser)
    add_model_file(parser, 'wb')


def add_hack(subparsers):
    parsers["hack"] = subparsers.add_parser("hack", help="Взломать")
    parser = parsers["hack"]
    add_model_file(parser, 'rb')
    add_files(parser)


def add_actions(parser):
    subparsers = parser.add_subparsers(dest="action", title='Доступные действия', required=True)
    add_encode(subparsers)
    add_decode(subparsers)
    add_train(subparsers)
    add_hack(subparsers)


def init_parse():
    parser = argparse.ArgumentParser(description="Шифратор")
    add_actions(parser)
    return parser.parse_args()
