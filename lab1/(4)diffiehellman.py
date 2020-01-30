import math
import random
import time

def eznum():


    while 1:
        z=0
        a=random.randint(1,500)
        for i in range(2,a,1):
            if a%i==1:
                continue
            if a%i==0:
                z=1
                break
        if z==0:
            break

    return a






def isPrime(n:int):
    if n < 1: raise ValueError(f"{n} < 1")
    return ~-2 ** n % n < 2





def powmod(a,b,c):

    z=1
    for i in range(0,b,1):
        z=z*a%c

    return z



def pubkey(G,A,P):
    pa=powmod(G,A,P)
    return pa

def Pvalue():
    while True:
        Q=eznum()
        P=2*Q+1
        if isPrime(P):
            print(f"{P} - not prime!")
        else:
            print(f"{P} - prime!")
            return P


def main():

    P=Pvalue()
    G=random.randint(1,P-1)
    A=random.randint(1,500)
    B=random.randint(1,500)
    ali=pubkey(G,A,P)
    bob=pubkey(G,B,P)
    ali1=pubkey(bob,A,P)
    bob1=pubkey(ali,B,P)
    print("P",P)


    print("G",G)
    print("A",A)
    print("B",B)
    print("PA",ali)
    print("PB",bob)
    print("Common key Alice",ali1)
    print("Common key Bob",bob1)

if __name__ == '__main__':
    main()