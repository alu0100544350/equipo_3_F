#!encoding: UTF-8
#!/usr/bin/python

import matplotlib.pylab as pl

x=[1,2,3,4,5]
#implementado
y1=[0.00396458305802,0.0441767826465,0.209839717571,0.431337197229,0.310562782005]
#algoritmo 
y2=[0.00396458305802,0.0441767826465,0.209839717571,0.431337197229,0.310562782005]
#implementado
y3=[0.00141382217407,0.00140905380249,0.00139784812927,0.0014019124512,0.00143218040466]
#algoritmo
y4=[0.000363388061523,0.000195741653442,0.000221014022827,0.000192880630493,0.000195026397705]

pl.subplot(211)
pl.plot(x,y1,'--',marker='*',label='implementado')
pl.plot(x,y2,':',color='r',marker='*',label='algoritmo')
pl.legend(loc=5)
pl.title('Resultados')
pl.xlabel('Valores')
pl.ylabel('Probabilidaes')


pl.subplot(212)
pl.xlabel('Valores')
pl.ylabel('Tiempo (s)')
pl.plot(x,y3,color='g',marker='*',label='implementado')
pl.plot(x,y4,marker='+',color='m',label='algoritmo')
pl.legend(loc=5)


pl.show()
