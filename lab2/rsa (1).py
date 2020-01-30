# Write Python3 code here 
from decimal import Decimal
import random
import pickle

def powmod(a,b,c):

    z=1
    for i in range(0,b,1):
        z=z*a%c

    return z

def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b)
    
def eznum():
    while 1:
        z=0
        a=random.randint(500,	1000)
        for i in range(2,a,1):
            if a%i==1:
                continue
            if a%i==0:
                z=1
                break
        if z==0:
            break

    return a
p = eznum()
q = eznum()
def cp():
    
    global n
    global e
    global ctt
    global d
    global t
    global mobs
    global mob1
    global mob2
    global mob3
    n = 10 ** 9
    mobs=[]*n
    mob1=[]*n
    mob2=[]*n
    mob3=[]*n
    
    
    f = open('1.png', 'rb')
    for line in f:
        print(line)
        for c in line:
            print(p)
            print(q)
            print(c)
            n = p*q 
            t = (p-1)*(q-1) 
            for e in range(2,t): 
                if gcd(e,t)== 1: 
                    break
            for i in range(1,p-1): 
                    x = 1 + i*t 
                    if x % e == 0: 
                        d = int(x/e)
                        break
            ctt = Decimal(0) 
            ctt =powmod(c,e,n)
            print('n = ',n)
            print('e = ',e)
            print('d = ',d)
            print('ctt = ',ctt)
            mobs.append(ctt)
            mob1.append(d)
            mob2.append(n)
            fs = 'key_rsa.dat'
            with open(fs, "wb") as file:
                pickle.dump(mob1, file)
                pickle.dump(mob2, file)
            fs = 'hifr_ctt.dat'
            with open(fs, "wb") as file:
                pickle.dump(mobs, file)
    
def dp():
    fs = 'hifr_ctt.dat'
    with open(fs, "rb") as file:
       m1= pickle.load(file)
    fs = 'key_rsa.dat'
    with open(fs, "rb") as file:
        m2=pickle.load( file)
        m3=pickle.load( file)
    
    for k in range(len(m1)):
            dtt = Decimal(0)
            dtt = powmod(m1[k],m2[k],m3[k])
            qw=dtt
            print(qw)
            print('decrypted text = ',dtt)
            mob3.append(qw)
            print(mob3)
    fs = 'rez_rsa.dat'
    with open(fs, "wb") as file:
        file.write(bytes(mob3))

def main():
    cp()
    dp()
    
    
    
    
if __name__ == '__main__': 
    main() 