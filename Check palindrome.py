# A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.

num=int(input("Enter any number to reverse it = "))
temp_num=num
reverse=0

while num!=0:
  reminder=num%10
  reverse=reverse*10+reminder
  num//=10
if reverse==temp_num:
  print("The given number is palindrome")
else:
  print("The given number is not palindrome")
