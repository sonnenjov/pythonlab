# Napišite program koji traži unos reči. Program 
# treba da ispiše sva slova reči, osim samoglasnika
#  (a, e, i, o, u). Iskoristite for petlju i continue da 
# # preskočite ispisivanje samoglasnika.

rec = input("Unesite neku rec: ")

for i in rec:
  if i in 'aeiou':
    continue
  print(f"{i}", end="")