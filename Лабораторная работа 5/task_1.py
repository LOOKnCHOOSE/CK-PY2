from pprint import pprint # загружаем модуль pprint
slovar = []
n = 16 # Для получения списка от до 15

for a in range(n):
    b = {'bin': bin(a), 'dec': a, 'hex': hex(a), 'oct': oct(a)} # Создание словаря от текущего значения
    slovar.append(b)

pprint(slovar)

