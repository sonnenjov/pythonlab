# Na programskom jeziku Python sastaviti program
#  koji ciklično proverava da li je uneti broj deljiv sa 3.
#  Unos nule ili negativnog broja prekida izvršavanje.


broj=int(input("Unesite broj koji zelite da proveravate da li je deljiv sa 3: "))

if broj <= 0:
  print("Uneti broj je negativan ili nula")
if broj%3!=0:
  print(f"Broj {broj} nije deljiv brojem 3")
else:
  print(f"Broj {broj} je deljiv brojem 3")


  