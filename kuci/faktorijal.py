# Napisati program u programskom jeziku Python koji
#  računava faktorijel broja n (n! = n * (n-1) * ... * 1).
#  Program treba da traži unos broja n od korisnika

broj = int(input("Unesite broj kom zelite da odredite fatktorijal: "))
faktorijalN=1
for i in range(1,broj+1):
  faktorijalN*=i
  print(f"i:{i}")
  print(f"fakt: {faktorijalN}")
  
print(f"Faktorijal broja {broj} je {faktorijalN}")