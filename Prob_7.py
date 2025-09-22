n=int(input("enter a number"))
def fabonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonacci(n-2) + fabonacci(n-1)
def fabonacciprint(n):
    i=0
    while i<n:
        print(fabonacci(i))
        i=i+1


print(fabonacciprint(n))


