import math


def aprox_seno(x:float,n:int)->float:
  suma:float=0.0
  for i in range(0,n+1):
        suma+= (((-1)**i)*(x**(2*i+1)/math.factorial(2*i+1)))
  real= math.sin(x)
  error=abs(suma-real)
  porcent_error= (error/real)*100

  print("aproximacion: "+str(suma))
  print("valor real: "+str(real))
  print("la diferencia es: "+str(error))
  print("el error porcentual es de "+str(porcent_error)+"%")

  if porcent_error<0.1:
    print("el porcentaje de error es menor que 0,1")
  else:
    print("el porcentaje de error es mayor que 0,1")
  
x=float(input("ingresa un numero real: "))
n=int(input("ingresa la cantidad de terminos a aproximar: "))

aprox_seno(x,n)