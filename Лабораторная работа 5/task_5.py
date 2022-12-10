from random import sample # Загружаем модуль sample

def get_password(n=8) -> str: # Функция создающая набор символов из источника
    hub = '0123456789ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' # Источник
    return "".join(sample(hub, n)) # Строка выбирает n символов из источника и убирает лишние симвлы


print(get_password())

