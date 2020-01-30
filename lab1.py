#from Biblio import eznum
import Biblio
import math
import random
import time
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
