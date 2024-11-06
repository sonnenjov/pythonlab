# list = [3,7,1,9,4]

# print(max(list))
# print(min(list))


list = [1,2,3,4,5,6,7,8,9,10]
sumaparnih=0
sumaneparnih=0
duzina = len(list)
for i in range(duzina):
  if list[i]%2==0:
    sumaparnih+=i
  else:
    sumaneparnih+=i
print("Suma parnih: ", sumaparnih)
print("Suma neparnih: ", sumaneparnih)