godine=int(input("Unesite broj godina vaseg radnog staza: "))

if(godine > 5):
  print("Ispunjava uslov za napredovanje")
else:
    print(f"Ne ispunjava uslov za napredovanje, treba jos {5-godine} godina")
    