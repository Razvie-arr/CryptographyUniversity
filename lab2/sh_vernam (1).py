from random import randint
import pickle

def cp():
    global crypt
    global keys
    global line
    global c
    global mobr
    global mobqw
    global mobz
    mobr=[]
    mobqw=[]
    mobz=[]
    f = open('1.png', 'rb')
    for line in f:
        print(line.strip())
        for c in line:
                crypt = ""
                keys = ""
                key = randint(0,255)
                keys += str(key) + " "
                gg = c + key
                crypt = chr( (gg) ) 
                mobr.append(crypt)
                mobz.append(keys)
                print(crypt)
                print(keys)
        
                print(mobr)
        fa = 'hifr_ver.dat'
        with open(fa, "wb") as file:
            pickle.dump(mobr, file)
        fa = 'key_ver.dat'
        with open(fa, "wb") as file:
            pickle.dump(mobz, file)
def dp():
    fs = 'key_ver.dat'
    with open(fs, "rb") as file:
       m1= pickle.load(file)
    fs = 'hifr_ver.dat'
    with open(fs, "rb") as file:
       m2= pickle.load(file)
   
    arr = []
    key=""
    for k in m1:
            if k != " ":
                    key += k
            else:
                    arr.append(key)
                    key=""
                    continue
    
    decrypt = ""
    for k in range(len(m2)):
        gg = ord(m2[k]) - int(m1[k])
        decrypt = ( (gg) )
        print(decrypt)
        print(key)
        mobqw.append(decrypt)
        fs = 'rez_ver.dat'
        with open(fs, "wb") as file:
            file.write(bytes(mobqw))
    
def main():
    cp()
    dp()
    
    
    
    
if __name__ == '__main__': 
    main() 
    

