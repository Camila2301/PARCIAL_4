"""El siguiente codigo calcula"""
"""Sumatoria del punto D"""
"""Autor:Maria Camila Vargas Giraldo"""
"""Ultima actualizacion:22 de septiembre/2021"""

x=6 #Podemos cambiar el valor de la variable si deseamos
n=5 #A continuacion ingresamos los n terminos que vamos a calcular
V=(((-1)**(1:n))*((x)**(2*1:n+1)))/((2*1:n-1)*(2*1:n))
1+sum(V)
