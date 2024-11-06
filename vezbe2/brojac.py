# brojac = 0

# broj = 1

# while(broj <= 20):
#   if broj%2==0 and broj%4==0:
#     brojac+=1
#   broj+=1

# print("Broj brojeva izmedju 1 i 20 koji su deljivi sa 2 i 4 je: ",brojac)

brojac = 0


for broj in range(1,21):
    if broj%2==0 and broj%4==0:
      brojac+=1
    broj+=1
    
print("Broj brojeva izmedju 1 i 20 koji su deljivi sa 2 i 4 je: ",brojac)
