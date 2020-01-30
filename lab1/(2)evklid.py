import math;
import random;
import time;

def evklid(a, b):

    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)

def main():

    a=random.randint(1,10)
    b=random.randint(1,10)

    print("a",a)
    print("b",b)
    print("evklid",evklid(a,b))



if __name__ == '__main__':
    main()