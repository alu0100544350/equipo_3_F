from scipy.stats import hypergeom
import numpy as np
import time

M=int(raw_input("Introduzca el valor de M: "))
n=int(raw_input("Introduzca el valor de n: "))
N=int(raw_input("Introduzca el valor de N: "))
x=int(raw_input("Introduzca el valor de x: "))
start = time.time()

rv = hypergeom(M, n, N)
pmf_cartas = rv.pmf(x)

print pmf_cartas

finish=time.time()-start

print finish