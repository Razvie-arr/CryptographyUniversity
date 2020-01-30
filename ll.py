import random
C=0
def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b)

def evklid(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
    return a

def eznum():
    while 1:
        z=0
        a=random.randint(500,1000)
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

def one(o):
    global C
    C = eznum()
    while True:
        if (evklid(C, F)) == 1:
            return (C)
    else:
        C = eznum()

Q=eznum()
P=eznum()
F=(P-1)*(Q-1)

def server():
    N=P*Q
    one(C)

    print("Генераторы: ")
    print("Q =", Q)
    print("P =", P)
    print("Ключи: ")

    print("C =", C)
    d = gcd(C, F) % F
    print("d = ", d)
    #print("D =", D)
    print("\nN =", N)
    print("F =", F)
    print("TIPOF",(P-1)*(Q-1))

server()
