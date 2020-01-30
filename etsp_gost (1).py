import math
import random 
import time
import binascii
from collections import Counter
import hashlib
import pickle

k=0
r=0
s=0

def gcd(a, b):

    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    #return (x, y, a)
    return (x)
def evklid(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
    return a

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

def mul(a,b,c):#a*b mod c 
    sum=0 
    for i in range(0,b,1): 
        sum+=a 

        if sum>=c: 
            sum-=c 
    return sum


def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
 
    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
 
    return r

    return z
def one(o):
    global d
    d = random.randint(3, F-1)
    while True:
        if (evklid(d, F))==1:
            return (d)
        else:
            d = random.randint(3, F - 1)
            
def get_hash_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)#8192
            if not data:
                break
            m.update(data)
        return m.hexdigest()

def mul(a,b,c):#a*b mod c 
    sum=0
     
    for i in range(0,b,1): 
        sum+=a 

        if sum>=c: 
            sum-=c 
    return sum

def isPrime(n:int):
    if n < 1: raise ValueError(f"{n} < 1")
    return ~-2 ** n % n < 2

def P_1():
    global q
    global b
    while True:
        q=eznum()
        b=random.randint(1,q)
        P=b*q+1
        if not isPrime(P):
            print(f"{P} - not prime!")
        else:
            print(f"{P} - prime!")
            return P
Z=P_1()


def gen_key():
    global y
    global r
    global s1
    global hash_int
    global Z
    global F
    global s
    global a
    global x
    mobs=[]
    mobs1=[]
    mobs2=[]
    while(1):
        print("p =",Z)
        print("q = ",q)
        g=random.randint(1,q)
        x=random.randint(1,q)
        #k=random.randint(1,q)
        a=pow_h(g,b,Z)
       
        print("a=",a)
        y=pow_h(a,x,Z)
       
        print("y=",y)
        z=get_hash_md5('asd.txt')
        print("hash md5: ",z)
        hash_int =int(z, 16)
        print("hash 10: ",hash_int)
        k=random.randint(1,q)
        r=pow_h(a,k,Z)%q
        print("r=",r)
        s=(k*hash_int+x*r)%q
        print("s=",s)
    
        if (r!=0 and s>0):
            break;
    mobs.append(z)
    mobs1.append(r)
    mobs2.append(s)
    fq = 'key_eg.dat'
    with open(fq, "wb") as file:
        pickle.dump(mobs, file)
        pickle.dump(mobs1, file)
        pickle.dump(mobs2, file)
def pro_key():

    fs = 'key_eg.dat'
    with open(fs, "rb") as file:
        m2 = pickle.load(file)  # z
        m3 = pickle.load(file)  # r
        m4 = pickle.load(file)  # s
    for k in range(len(m2)):
        b = int(m2[k], 16)
        u1 = (m4[k] * gcd(b, q)) % q
        u2 = q - ((m3[k] * gcd(b, q)) % q)
        v = ((pow_h(a, u1, Z) * pow_h(y, u2, Z)) % Z) % q
        print("v=", v)
        if(m3[k] == v):
            print('Success!')

def main():
    gen_key()
    pro_key()
    
    
    
    
if __name__ == '__main__': 
    main() 