broj = int(input("Unesite broj: "))
suma=0
i=1
while(i<broj):
  if broj%i==0:
    suma+=i
  i+=1
if broj==suma:
  print(f"Broj {broj} je savrsen")
else:
  print(f"Broj {broj} nije savrsen")
    
