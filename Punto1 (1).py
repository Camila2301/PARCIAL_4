"""El siguiente codigo calcula e imprime"""
"""Sumatoria de Riemann"""
"""Autor:Maria Camila Vargas Giraldo"""
"""Ultima actualizacion:22 de septiembre/2021"""

import numpy as np 
def Zeta(n):
	r=0 # inicializo la variable que va a guardar la suma
	for i in range(1,n+1): # este ciclo hace la sumatoria 
		r=r+(i**(-2)) # se está sumando r que guarda la sumatoria hasta i-1 con el i-esimo termino.
	return r
# viendo la aproximación 
print((Zeta(10000)))
print((np.pi**2)/6)







