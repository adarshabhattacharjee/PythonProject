n=input("enter the number")
print("Input : ",n)
print('Output:')
i=0
for i in range(1, int(n)+1):
    print(" " * (int(n) - i) + "* " * i)
for i in range(int(n) - 1, 0, -1):
    print(" " * (int(n) - i) + "* " * i)

