import math
import random 
import time
import pickle
import binascii
from collections import Counter

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


def powmod(a,b,c):

    z=1
    for i in range(0,b,1):
        z=z*a%c

    return z
p = eznum()
def encrypt():
    n = 10 ** 9
    global p
    global cb
    global r
    global e
    global m
    global za
    global keys
    global line
    global c
    global zs
    global mobs
    global g
    global k
    global p
    global mobsg
    global mobscb
    global mobsr
    global mobsk
    global mobqw
    
    mobs = []
    mobsg=[]
    mobscb=[]
    mobsk=[]
    mobsr=[]
    mobqw=[]
    
    f = open('1.png', 'rb')
    for line in f:
        print(line)
        for c in line:#считывание строки в файле
                g = random.randint(1, p - 1)
                cb = random.randint(1, p - 1)
                k = random.randint(1, p - 2)
                db = powmod(g, cb, p)
                print("db =", db)
                #r = powmod(g, k, p)
                e = mul(powmod(db, k, p), c, p)
                print("e=",e)
                r = powmod(g, k, p)
                mobs.append(e)
                mobsg.append(g)
                mobscb.append(cb)
                mobsk.append(k)
                mobsr.append(r)
        
        print("ss",mobs)
        fa = 'hifr_eg.dat'
        with open(fa, "wb") as file:
            pickle.dump(mobs, file)
            
        file.close()
        fq = 'key_eg.dat'
        with open(fq, "wb") as file:
            pickle.dump(mobsg, file)
            pickle.dump(mobscb, file)
            pickle.dump(mobsk, file)
            pickle.dump(mobsr, file)
        
    
    #print("r =", r)
        
    #print("e =", e)
            
        
def decrypt():
    global key
    global keys
    global mylist
    fs = 'hifr_eg.dat'
    with open(fs, "rb") as file:
       m1= pickle.load(file)
    fs = 'key_eg.dat'
    with open(fs, "rb") as file:
        m2=pickle.load( file)
        m3=pickle.load( file)
        m4=pickle.load( file)
        m5=pickle.load( file)
    
    
    for k in range(len(m1)):
            deM = mul(m1[k], powmod(m5[k], p - 1 - m3[k], p), p)
            print("Decrypted222 =", deM)
            qw=deM
            print(qw)
            mobqw.append(deM)
            print(mobqw)
    fs = 'rez_eg.dat'
    with open(fs, "wb") as file:
        file.write(bytes(mobqw))
            
    
    


def main():
    encrypt()
    decrypt()
    
    
    
    
if __name__ == '__main__': 
    main() 




 
    
   


  
  
  
     
  
  
