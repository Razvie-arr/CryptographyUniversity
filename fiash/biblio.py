import random
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


def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module

    return r
