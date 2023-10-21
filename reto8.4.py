n=int(input("ingresa el numero hasta el cual quieres el factorial: "))
i=1
factorial=1
for i in range(1,n+1):
  factorial *=i
  print("el factorial del numero "+str(i)+ " es "+str (factorial))
  i +=1