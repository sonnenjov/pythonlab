# 8. zadatak
#   Marina pravi plan trošenja džeparca tokom letovanja od 14 
# dana. Napišite program koji za prosečne dnevne potrošnje od 
# 5, 10 ili 20 evra ispisuje koliko bi u svakom od tih slučajeva
#  Marini ukupno trebalo novca.

broj_dana=14

for i in range(5,10,20):
  ukupno=broj_dana*i
  print(f"Ako marina trosi {i} dnevno, za 14 dana ce joj biti potrebno {ukupno} evra")