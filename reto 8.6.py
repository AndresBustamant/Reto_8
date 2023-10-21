n=int(input("ingresa la base de la potencia: "))
x=int(input("ingresa el exponenete de la potencia"))
potencia=1
for i in range(x):
  potencia *=n
print("para la base "+str(n)+ " elevada a "+str(x) +" la potencia es igual a: "+str (potencia))