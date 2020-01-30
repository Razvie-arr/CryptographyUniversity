import random
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def eznum():
    while 1:
        z=0
        a=random.randint(100,1000)
        for i in range(2,a,1):
            if a%i==1:
                continue
            if a%i==0:
                z=1
                break
        if z==0:
            break

    return a

def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module

    return r


def Dfind():
    global D
    D = random.randint(1, F)
    while True:
        for e in range(2, F):
            if gcd(C, F) == 1:
                return D
def Сfind():

    while True:
        if ((C*D)%(F))==1:
            return (C)
        else:
            С = random.randint(1, 100000)
C=0
Q=eznum()
P=eznum()
F=(P-1)*(Q-1)
def server():
    N=P*Q
    Dfind()
    Сfind()
    print("Генераторы: ")
    print("Q =", Q)
    print("P =", P)
    print("Секретные ключи: ")
    print("C =", C)
    print("D =", D)
    print("\nN =", N)
    print("F =", F)

def client():
    rnd=random.randint(1, )




server()
client()



"""если ничего не работает, то нужно поправить взаимную простоту"""