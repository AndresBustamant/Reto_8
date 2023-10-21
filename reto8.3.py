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