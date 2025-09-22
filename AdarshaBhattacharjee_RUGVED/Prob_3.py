num=int(input("Enter a number: "))
s=str(num)
sn= float(len(s))
if sn<3:
    print("not a hill number")

i=0
while i<sn and s[i]<s[i+1]:
     i+=1
     print("not a hill number")

while i<sn and s[i]>s[i+1]:
     print("not a hill number")

while i + 1 < sn and s[i] > s[i + 1]:
     i += 1
     print("not a hill number")
else :
     print("It is a hill number")


