# Reto_8

buenas noches, en este repisitorio encontraras el desarrollo del reto 8, espero sea de su agrado.


link notebook: https://colab.research.google.com/drive/1XcQubCADOGhIpBwFJWqZ1bjVO9KejaEu?usp=sharing



1.Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

desarrollo: para este punto desarrolle un programa a el cual se le indique el numero del cual se quiere el cudrado y lo clacule a partir de un rango establecido.

```pseudocode
cuadrado=0
n=0
for n in range (0,101):
  cuadrado= n**2
  print("el cuadrado de "+str(n)+ " es "+ str(cuadrado))
  n +=1
```

2.Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

desarrollo: para este punto empece por definir dos listas y un numero en el cual se evaluara aumentando en un rango de 1-100o con el fin de ver si es par o no 
y asi mismo ubicarlo en una de las dos listas ordenas.

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

desarrollo: el programa en este punto empieza por solicitar un numero y evalua primero si es par o impar, en el caso de ser impar lo vuelve par, esto con el fin de ir restando de a dos unidades dentro de un rango establecido entre el numero n y 2.

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

desarrollo: este punto se basa en solicitar un numero y a partir de este calcular y mostrar el factorial entendiendolo como una multiplicacion consecutiva hasta el mayor valor que toma el rango establecido.

```pseudocode
n=int(input("ingresa el numero hasta el cual quieres el factorial: "))
i=2
factorial=1
for i in range(1,n+1):
  factorial *=i
  print("el factorial del numero "+str(i)+ " es "+str (factorial))
  i +=1
```

5.Calcular el valor de 2 elevado a la potencia n usando ciclos for.

desarrollo: el programa de este punto a partir de un numero solicitado empieza a mostrar los numeros elevados a la potencia 2

```pseudocode
n=int(input("ingresa el numero hasta el cual quieres la potencia: "))
i=1
potencia=2
for i in range(1,n+1):
  potencia *=2

print("la el numero "+str(i)+ " elevado a el cuadrado es "+str (potencia))
```

6.Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

desarrollo: este punto bsa su desarrollo con la misma ide del entarior, el cambio que se hace para cumplir el objetivo es cambiar la potencia a la que se va a elevar

```pseudocode
n=int(input("ingresa la base de la potencia: "))
x=int(input("ingresa el exponenete de la potencia"))
potencia=1
for i in range(x):
  potencia *=n
print("para la base "+str(n)+ " elevada a "+str(x) +" la potencia es igual a: "+str (potencia))
```

7.Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

desarrollo: en este punto utilize dos ciclos for el primero con el fin de dar el numero de referencia de la tabla y el segundo para operar el numero anterior con cada numero de 1-10

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

desarrollo: para este punto cree una funcion delimitada por dos valores solictados en la cual a partir de un rango evaluara de forma aproximada la funcion exponencia y de manera simultanea calculara el valor real y los diferenciara para entender el porcetaje de error presente.

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

desarrollo:para este punto cree una funcion delimitada por dos valores solictados en la cual a partir de un rango evaluara de forma aproximada la funcion seno y de manera simultanea calculara el valor real y los diferenciara para entender el porcetaje de error presente.


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

desarrollo: por ultimo cree un programa delimitado a los valores de la tangenete (-1,1) el cual evalua de forma aproximada los valores que se pueden dar y posterior menete los compara con el valor real, dando como resultado el porcentaje de error en el calculo.

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
Gracias por leer hasta aqui.
