# Task 5.2
"""
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:

In [1]: "1" * 28 + "0" * 4
Out[1]: "11111111111111111111111111110000"
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Сестра, несите тазик. Тазик эвтаназик/24: ')
mask = ip[(ip.find('/') + 1):]
mask_bin = '1' * mask + '0' * (32 - mask)
# mask_bin[1:9]
# int(mask_bin[1:9], 2)
#ip = ip.find('/')
