broj = int(input("Unesite celi broj"))

if broj%3==0 and broj%5==0:
    print("broj je deljiv sa 5 i 3")

elif broj%5==0:
  print("Broj je deljiv sa 5")
elif broj%3==0:
  print("Broj je deljiv sa 3")
else:
  print("Broj nije deljiv ni sa 5 ni sa 3")  
