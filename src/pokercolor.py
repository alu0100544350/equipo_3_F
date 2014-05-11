#!encoding:UTF-8
#!/usr/bin/python

import math
import time

start1 = time.time()

def fact(p):
    a=1
    if p<0:
        return 0
    elif p==0:
        return 1
    else:
        for i in range(2,p+1):
            a=a*i
    return (a)
finish1 = time.time()-start1

N1=int(raw_input("Introduzca el número de cartas de determinado palo :"))
N2=int(raw_input("Introduzca el número de cartas de los otros tres palos :"))
n=int(raw_input("Introduzca el número de cartas extraídas de la baraja :"))
x=int(raw_input("Introduzca el número de cartas extraidas de un determinado palo :"))
N=N1+N2

start2=time.time()

comb1=float(fact(N1)/(fact(x)*fact(N1-x)))
comb2=float(fact(N2)/(fact(n-x)*fact(N2-n+x)))
comb3=float(fact(N)/(fact(n)*fact(N-n)))

probabilidad=(comb1*comb2)/comb3
print"La probabilidad es : ",probabilidad

finish2= time.time() - start2

finish = finish1 + finish2

print "El tiempo que tarda en ejecutarse es de: ", finish