#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import socket
import biblio
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # реализация сокета
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
p = biblio.eznum()  # генерируем простое число p
q = biblio.eznum()  # генерируем простое число q
with open('open keys.txt', 'w', encoding='utf-8') as f:  # запись p и q в файл
    print((str)(p), "\n", (str)(q), file=f)
with open('open keys.txt') as file:  # чтение из файла
    p = int(file.readline())
    q = int(file.readline())
n = p * q
conn.send((str)(n).encode('utf-8'))  # отправляем n
data1 = conn.recv(16384)  # получаем v
str1 = (data1.decode('utf-8'))
v = int(str1)
f.close()
for i in range(1, 41):
    print("КОНЕЦ " + (str)(i) + " РАУНДА")
    print("Открытый ключ p равен:", p)
    print("Открытый ключ q равен:", q)
    print("Открытый ключ v равен:", v)
    nade = ((1 / 2) ** i *100)
    data1 = conn.recv(16384)  # получаем x
    str1 = (data1.decode('utf-8'))
    x = int(str1)
    print("x = ", x)
    e = random.randint(0, 1)  # генерируем и отправляем e
    print("e = ", e)
    conn.send((str)(e).encode('utf-8'))
    data2 = conn.recv(16384)  # получаем y
    str2 = (data2.decode('utf-8'))
    y = int(str2)
    print("y = ", y)
    rez = ((x * biblio.pow_h(v, e, n)) % n)  # вычисляем x*v ** e (mod n)
    reliability=100-nade
    print("y ** 2 = x*v ** e (mod n)", (y ** 2) % n == rez)
    if ((y ** 2) % n) == rez:  # проверка
        print("Протокол Фиата-Шамира успешно выполнен")
        print("Надежность системы: " + (str(reliability)) + "%\n\n\n")

sock.close()
