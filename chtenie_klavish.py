import math
import random 
import time
import pickle
import binascii
from collections import Counter
p=random.randint(1,20)
ca=0
da=0
cb=0
db=0
def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module

    return r

    return z
def eznum():
    while 1:
        z=0
        a=random.randint(1000,100000)
        for i in range(2,a,1):
            if a%i==1:
                continue
            if a%i==0:
                z=1
                break
        if z==0:
            break

    return a

def evklid(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
    return a

def vzaimprime(a, b):
    return evklid(a, b)==1

def one(o):
    global da
    da=0
    while True:
        if ((ca*da)%(p-1))==1:
            return (da)
        else:
            da = random.randint(10, p - 1)

def two(n):
    global db
    db=0
    while True:
        if ((cb*db)%(p-1))==1:
            return (db)
        else:
            db = random.randint(10, p - 1)

def gen_deck():
    houses = ['S', 'C', 'H', 'D']
    cards = ['0' + str(i) if len(str(i)) == 1 else str(i)
             for i in range(2, 11)]
    cards.extend(ord(face_card) for face_card in ['K', 'Q', 'J', 'A'])
    deck = []
    for house in houses:
             deck.extend([int((str(ord(house)) + str(card))) for card in cards])

    return deck

def read_card(card):
    card = str(card)
    house = chr(int((card[0:2])))
    num = card[2:]
    num = int(num) if int(num) <= 10 else chr((int(num)))
    houses = {'S': 'Spades', 'C': 'Clubs', 'H': 'Hearts', 'D': 'Diamonds'}
    return str(num) + ' of ' + houses[house]


deck = gen_deck()
"""cards = [read_card(card) for card in deck]

print ("\nКарты:\n")
print (cards)

print ("\n\nЧсиловое значение карт для работы с ними:\n")
print (deck)"""


p=23
c1=7
d1=10
c2=9
d2=5
mm=[]
g =  int(input("### kol Igorei? \n"))
for x in range(g):
    for i in deck:
        z=i
        mm.append(z)
        random.shuffle(mm)

    print("Карты[g]\n",mm)
    #mm.clear()
    #cards = [read_card(card) for card in mm]
    #print ("\nТУса карты:\n")
    #print (cards)
p=eznum()
ca=eznum()
cb=eznum()
class Player:
    def gen(self):
        one(da)
        two(db)
    def cod(self):
        newdeck=[]
        for ()


    def shuffle_deck(deck):
        random.shuffle(deck)
        return deck

    gen()
    cod()
    shuffle_deck()
