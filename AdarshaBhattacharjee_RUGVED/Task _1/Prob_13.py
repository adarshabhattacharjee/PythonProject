arr=input("input an array")
def firstRepeatingElement(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return i
    return 0
n = len(arr)
index = firstRepeatingElement(arr, n)
if index == 0:
      print("No repeating element found!")
else:
      print("First repeating element is", arr[index])