num = input("Write me a number")
collect=set()
x = 1

if num.isnumeric():
  num = int(num)
  while x <= num:
    if (num%x) == 0:
      collect.add(x)
    x +=1
  if {num,1}==collect:
    print("This is a primary number.")
  else:
    print("This is not a primary number")
else:
  print("Plesea write just a numeric")
