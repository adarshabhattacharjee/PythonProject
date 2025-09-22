string=input("Enter a string: ")
sort=''.join(sorted(string))
current_char = sort[0]
count = 0

for char in sort:
    if char == current_char:
        count += 1
    else:
        print(f"{current_char}: {count}")
        current_char = char
        count = 1