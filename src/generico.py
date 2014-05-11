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

finish1 = time.time() - start1     
        
A=int(raw_input("Introduzca el A (A>x): "))
B=int(raw_input("Introduzca el B (B>n-x): "))
n=int(raw_input("Introduzca el n: (n<A+B)"))
x=int(raw_input("Introduzca la x: "))
start2 = time.time()
N=A+B

comb1=float(fact(A)/(fact(x)*fact(A-x)))
comb2=float(fact(B)/(fact(n-x)*fact(B-n+x)))
comb3=float(fact(N)/(fact(n)*fact(N-n)))

probabilidad=(comb1*comb2)/comb3

print"La probabilidad es :",probabilidad

finish2 = time.time() - start2

finish = finish1 + finish2

print finish