

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



def evklid(a, b):

    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)



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
