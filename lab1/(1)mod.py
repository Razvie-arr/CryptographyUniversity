import math;
import random;
import time;

def eznum():


    while 1:
        z=0
        a=random.randint(1,5000000)
        for i in range(2,a,1):
            if a%i==1:
                continue
            if a%i==0:
                z=1
                break
        if z==0:
            break

    return a;


def powmod(a,b,c):

    z=1
    for i in range(0,b,1):
        z=z*a%c

    return z






def main():

    a=random.randint(0,500000)
    c=eznum()
    b=random.randint(1,c-1)


    print("a",a)
    print("b",b)
    print("c",c)
    print("rez",powmod(a,b,c))


if __name__ == '__main__':
    main()