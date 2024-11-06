def ref_demo(x):
  print("x=",x,"x(id)= ", id(x))
  
demo = ref_demo(5)

print(id(4))