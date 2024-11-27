num=int(input("Enter any number to chech Armstrong = "))
c=str(num)
length=(len(c))
b=num
sum=0

print("lenght is =", length)

while b!=0:
  rem=b%10
  sum=sum+rem**length
  b//=10
if num==sum:
  print("The given number is armstrong")
else:
  print("The given number is not armstrong")
