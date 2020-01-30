import math
import random
import time
import pickle

x=0
y=0
p=0
da=0
db=0
def evklid(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
    return a
def eznum():
    while 1:
        z=0
        a=random.randint(9000,10000)
        for i in range(2,a,1):
            if a%i==1:
                continue
            if a%i==0:
                z=1
                break
        if z==0:
            break

    return a



def powmod(a,b,c):

    z=1
    for i in range(0,b,1):
        z=z*a%c

    return z

def vzaimprime(a, b):
    return evklid(a, b)==1

def cip(a,b,c):
    global ca
    global cb
    global p
    x=eznum()
    y=eznum()
    p=eznum()
    if (vzaimprime(x, p)&vzaimprime(y, p))==True:
            ca=x
            cb=y
            return (ca, cb, p)
def one(o):
    global da
    da=0
    while True:
        if ((ca*da)%(p-1))==1:
            return (da)
        else:
            da = random.randint(10, p - 1)

def two(n):
    global db
    db=0
    while True:
        if ((cb*db)%(p-1))==1:
            return (db)
        else:
            db = random.randint(10, p - 1)


def encrypt():
    global mobe
    
    mobs = [] 
    mobsg=[] 
    mobscb=[] 
    mobsk=[]
    mobsr=[]
    mobsz=[]
    mobe=[]
    
    f = open('ww.dat', 'rb')
    for line in f:
        print(line)
        for c in line:
            (cip(x,y,p))
            print("Ca =",ca)
            print("Cb =",cb)
            print("P =",p)
            one(da)
            print("da =", da)
            print("(ca*da)%(p-1)) =",(ca*da)%(p-1))
            two(db)
            print("db =", db)
            print("(cb*db)%(p-1)) =", (cb * db) % (p - 1))
            mobs.append(c)
            mobsg.append(ca)
            mobscb.append(cb)
            mobsk.append(da)
            mobsr.append(db)
            mobsz.append(p)
        
 
        print("ss",mobs)
        fa = 'hifr_sh.dat'
        with open(fa, "wb") as file:
            pickle.dump(mobs, file)
        fa = 'key_sh.dat'
        with open(fa, "wb") as file:
            pickle.dump(mobsg, file)
            pickle.dump(mobscb, file)
            pickle.dump(mobsk, file)
            pickle.dump(mobsr, file)
            pickle.dump(mobsz, file)
            

def decrypt():
    global key
    global keys
    global mylist
    global x1
    fs = 'hifr_sh.dat'
    with open(fs, "rb") as file:
       m1= pickle.load(file)#mobs
    fs = 'key_sh.dat'
    with open(fs, "rb") as file:
        m2=pickle.load( file)#mobsg
        m3=pickle.load( file)#mobscb
        m4=pickle.load( file)#mobsk
        m5=pickle.load( file)#mobsr
        m6=pickle.load( file)#mobsz
    for k in range(len(m1)):
            x1=powmod(m1[k],m2[k],m6[k])
            print("x1 =", x1)
            x2=powmod(x1,m3[k],m6[k])
            print("x2 =", x2)
            x3=powmod(x2,m4[k],m6[k])
            print("x3 =", x3)
            x4=powmod(x3,m5[k],m6[k])
            print("x4 =", x4)
            qw=x4
            print(qw)
            mobe.append(qw)
            fa = 'rez_sh.dat'
            with open(fa, "wb") as file:
                file.write(bytes(mobe))
    #if x4==m:
        #print("SUCCESS!")
                
            
            
    
    

def main():
    encrypt()
    decrypt()
if __name__ == '__main__':
        main()

