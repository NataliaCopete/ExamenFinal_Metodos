# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)
valor=x[0]
i=0
while(valor<800.0):
    if(valor%2!=0):
      print(valor)
    i=i+1
    valor=x[i]
    



