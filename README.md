# Reto_8

buenas noches, en este repisitorio encontraras el desarrollo del reto 8, espero sea de su agrado 


link notebook: https://colab.research.google.com/drive/1XcQubCADOGhIpBwFJWqZ1bjVO9KejaEu?usp=sharing



1.Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

desarrollo:

```pseudocode
cuadrado=0
n=0
for n in range (0,101):
  cuadrado= n**2
  print("el cuadrado de "+str(n)+ " es "+ str(cuadrado))
  n +=1
```

2.Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

desarrollo:

```pseudocode
n=0
impares=[]
pares=[]
for n in range (0,1001):
  if n%2==0:
    pares.insert(0,n)
    pares1= sorted(pares)
  else:
    impares.insert(0,n)
    impares1= sorted(impares)
  n+=1
print("los numeros pares son: ")
print(pares1)
print("los numeros impares son: ")
print(impares1)
```

3.Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

desarrollo:

```pseudocode
n=int(input("ingresa el numero hasta el cual quieres los numeros de forma descendente: "))
if n%2==0:
  n=n
else:
  n==n-1
pares=[]
for i in range (2,n+1):
     pares.insert(0,n)
     n-=2
     if n ==0:
      break

print("los numeros pares de forma descendente son: ")
print(pares)
```

4.Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

desarrollo:

```pseudocode
n=int(input("ingresa el numero hasta el cual quieres el factorial: "))
i=1
factorial=1
for i in range(1,n+1):
  factorial *=i
  print("el factorial del numero "+str(i)+ " es "+str (factorial))
  i +=1
```

5.Calcular el valor de 2 elevado a la potencia n usando ciclos for.

desarrollo:

```pseudocode
n=int(input("ingresa el numero hasta el cual quieres la potencia: "))
i=1
potencia=1
for i in range(1,n+1):
  potencia *=2

print("la el numero "+str(i)+ " elevado a el cuadrado es "+str (potencia))
```

6.Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

desarrollo:

```pseudocode
n=int(input("ingresa la base de la potencia: "))
x=int(input("ingresa el exponenete de la potencia"))
potencia=1
for i in range(x):
  potencia *=n
print("para la base "+str(n)+ " elevada a "+str(x) +" la potencia es igual a: "+str (potencia))
```

7.Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

desarrollo:

```pseudocode
for i in range(1,11):
  print("la tabla de "+str(i)+ " es: ")
  for h in range(0,11):
    tabla= i*h
    print(tabla)
    h+=1
```

8.Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

![formula 1](https://github.com/AndresBustamant/Reto_8/assets/141858005/8b8c5239-be8f-47a8-873a-19030dcab11e)

desarrollo:

```pseudocode
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
```

9.Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

![formula 2](https://github.com/AndresBustamant/Reto_8/assets/141858005/8e6966cf-0f96-4b52-b2c8-86fb2f4bbe97)

desarrollo:

```pseudocode
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
```

10.Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

![formula 3](https://github.com/AndresBustamant/Reto_8/assets/141858005/9001e9fe-a5f4-4488-bbe1-4d4fc414a798)

desarrollo:

```pseudocode
import math

def aprox_arcotangente(x:float,n:int)->float:
  suma:float=0.0
  for i in range(-2,2):
        suma+= (((-1)**i)*(x**(2*i+1)/(2*i+1)))
  real= math.atan(x)
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

aprox_arcotangente(x,n)
```
