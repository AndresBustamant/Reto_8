n=0
impares=[]
pares=[]
for n in range (0,101):
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