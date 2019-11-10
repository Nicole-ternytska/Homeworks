import re

def is_int (text):
    return bool(re.match(r'^[-+]?\d+$',text))

def is_float_pos (text):
    return bool(re.match(r'^[^-]\d+\.?\d*$',text))

def is_float (text):
    return bool(re.match(r'^[-+]?\d+\.?\d*$',text))

def int_val (text = 'Введіть число: '):
    number = input(text)

    while not is_int(number):
        number = input(text)
    return int(number)

def float_val_pos (text = 'Введіть число: '):
    number = input(text)

    while not is_float_pos(number):
        number = input(text)
    return float(number)

def float_val (text = "Введіть число: "):
    number = input(text)

    while not is_float(number):
        number = input("Введіть число: ")
    return float(number)