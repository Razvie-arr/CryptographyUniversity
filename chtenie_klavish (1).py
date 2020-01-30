import math
import random 
import time
import pickle
import binascii
from collections import Counter

ca=0
da=0
cb=0
db=0
def eznum():
    while 1:
        z=0
        a=random.randint(1000,10000)
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

def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
 
    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
 
    return r


def one(o):
    global da
    da=0
    while True:
        if ((ca*da)%(p-1))==1:
            return (da)
        else:
            da = random.randint(1, p - 1)

def two(n):
    global db
    db=0
    while True:
        if ((cb*db)%(p-1))==1:
            return (db)
        else:
            db = random.randint(1, p - 1)

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

ss=[]
ss1=[]
deck = gen_deck()
cards = [read_card(card) for card in deck]

#print ("\ncard‹:\n")
#print (cards)

#print ("\n\nznah card:\n")
#print (deck)

p=eznum()
ca=eznum()
cb=eznum()
class Player(object):
    def cod(self):
        one(da)
        two(db)
    def enca(self,deck):
        decky = []
        for card in deck:
            decky.append(pow_h(card,ca,p))
        return decky
    def encb(self,deck):
        decky = []
        for card in deck:
            decky.append(pow_h(card,cb,p))
        return decky
    
    def shuffle(self,deck):
        random.shuffle(deck)
        return deck
one(da)
two(db)
print("p=",p)
print("ca=",ca)
print("cb=",cb)
print("da=",da)
print("db=",db)

dima=Player()
vlad=Player()

deck=dima.enca(deck)
deck=dima.shuffle(deck)
print(deck)

deck=vlad.encb(deck)
deck=vlad.shuffle(deck)
print(deck)

dima=random.choices(deck,k=3)
print(dima)

for k in range(len(dima)):
    s=pow_h(dima[k],db,p)
    ss.append(s)
print(ss)
for k in range(len(ss)):
    s1=pow_h(ss[k],da,p)
    ss1.append(s1)
print (ss1)

    

