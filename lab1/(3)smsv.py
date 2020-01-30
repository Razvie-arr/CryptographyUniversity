import math;
import random;
import time;


def powmod(a,b,c):
    z=1
    for i in range(0,b,1):
        z=z*a%c
    return z;


def eznum():


    while 1:
        z=0
        a=random.randint(1,50000)
        for i in range(2,a,1):
            if a%i==1:
                continue
            if a%i==0:
                z=1
                break
        if z==0:
            break

    return a;


def sbsg(a,b,y):
    n=int(math.sqrt(y)+1)

    dar=[0]*y

    for i in range(0,n,1):
        for j in range(0,n,1):
            dar[powmod(a,i*n,y)]=i
            mas=(powmod(a,j,y)*b)%y

            if dar[mas]:
                ex=dar[mas]*n-j
                if ex<y:
                    return ex
                else:
                    print("error!!!")
    else:
        print("error!!!")
        return 0


def main():

    a=random.randint(0,50000)
    c=eznum()
    b=random.randint(1,c-1)




    print("a",a)
    print("b",b)
    print("c",c)
    print("rez",powmod(a,b,c))
    print("sbsg",sbsg(a,b,c))

if __name__ == '__main__':
    main()