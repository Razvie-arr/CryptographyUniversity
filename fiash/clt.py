#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import socket
import biblio
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))  # подключаемся к серверу
data1 = sock.recv(16384)  # получаем n
str1 = (data1.decode('utf-8'))
n = int(str1)

secret = random.randint(1, n - 1)  # генерация закрытого ключа
while True:  # проверка на взаимную простоту secret и n
    if biblio.evklid(secret, n) == 1:
        break
    else:
        secret = random.randint(1, n - 1)
v = biblio.pow_h(secret, 2, n)  # генерация открытого ключа
sock.send(str(v).encode('utf-8'))  # отправляем v
for i in range(1, 41):
    print("КОНЕЦ " + str(i) + " РАУНДА")
    print("n равен:", n)
    print("Закрытый ключ s равен:", secret)
    print("Открытый ключ v равен:", v)
    r = random.randint(1, n - 1)  # генерируем r, далее вычисляем x и отправляем серверу
    print("r = ", r)
    x = biblio.pow_h(r, 2, n)
    print("x = ", x)
    sock.send(str(x).encode('utf-8'))
    data2 = sock.recv(1000000)  # получаем e
    str2 = (data2.decode('utf-8'))
    e = int(str2)
    print("e = ", e)
    if e == 0:
        y = r
    else:
        y = biblio.pow_h(r * secret, 1, n)  # вычисляем и отправляем y
    print("y = ", y)
    sock.send(str(y).encode('utf-8'))
    print("<------ Вывод там  \n\n\n")
sock.close()
