import math


def aprox_exponencial(x:float,n:int)->float:
  suma:float=0.0
  for i in range(0,n+1):
        suma+= x**i/math.factorial(i) 
  real= math.exp(x)
  error=abs(suma-real)
  porcent_error= (error/real)*100

  print("aproximacion: "+str(suma))
  print("valor real: "+str(real))
  print("la diferencia es: "+str(error))
  print("el error porcentual es de "+str(porcent_error)+"%")

  while porcent_error<0.1:
    print(aprox_exponencial)
  
x=float(input("ingresa un numero real: "))
n=int(input("ingresa la cantidad de terminos a aproximar: "))

aprox_exponencial(x,n)