a=10
def spolja_funkcija():
  a=20
  def unutrasnja():
    a=30
    print('a = ',a)
  unutrasnja()        
  print('a = ',a)
        

spolja_funkcija()