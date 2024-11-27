n = int(input("Enter any number to check that is prime or not = "))
flag=True
i = 2
while i<n:
    if n%i == 0:
        flag = False
        break
    i+=1
if flag==True:
    print(f'The given number "{n}" is Prime')
else:
    print(f'The given number "{n}" is not Prime')
