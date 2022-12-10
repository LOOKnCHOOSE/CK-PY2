from random import randint

def unique_numbers() -> list[int]:
    get_numbers = [randint(-10, 10) for _ in range(15)] # Получаем 15 рандомных чисел

    unique = set(get_numbers) # Получаем уникальные числа данного списка

    while len(unique) < 15: # Запускаем цикл, который будет добавлять
        # случайное число в наш список, пока количество уникальных чисел в списке не
        # будет равным 15
        unique = list(unique)
        unique.append(randint(-10, 10))
        unique = set(unique)
    return list(unique)


print(unique_numbers())

