number=int(input("Enter a number to find factorial = "))
factorial=1

while number>0:
  factorial=factorial*number   # 5*1=5    4*5=20  =   20*3=60     60*2= 120    120*1=120
  number-=1
print("Factorial value of given number is =", factorial)
