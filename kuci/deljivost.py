brojac=0
for i in range(1,20):
    if i%2==0 and i%4==0:
      print(f"Number {i} is divisible with 2 and 4")  
      brojac+=1
    elif i%2==0:
      print(f"Number {i} is divisible with 2 ")
      brojac+=1  
    elif i%4==0:
      print(f"Number {i} is divisible with 4")
      brojac+=1
    else:
      print(f"Number {i} can not be divided neither with 4 nor 2;")  
      
      
print(f"Broj brojeva koji su deljivi sa 2 i 4 u rasponu od 1 do 20 je: {brojac}")