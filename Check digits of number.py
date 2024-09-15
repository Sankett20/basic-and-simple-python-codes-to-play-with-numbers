# WAP to find the count of digits in a given number.
num=int(input("Enter a multiple digit number ="))
count=0

while num!=0:
  count+=1
  num//=10
print("Number of digits in given number =", count)
