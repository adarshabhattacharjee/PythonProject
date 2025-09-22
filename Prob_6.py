
'''
checking whether a string is an anagram or not is not
possible as python can't comprehend words out of it's 
domain, but we can check whether the two strings
provided are anagram or not 
'''

str_1=input("enter a string")
str_2=input("enter another string")
if sorted(str_1)==sorted(str_2):
  print("yes, they are anagram")
else:
  print("no, they are not anagram")

