broj=int(input("Unesite broj"))
temp=0
while broj>0:
  temp=temp*10 + broj%10
  broj//=10 #obavezno celobrojno deljenje, kada se radi samo jedna crta deljenja ispada nesto drugo


print(temp)