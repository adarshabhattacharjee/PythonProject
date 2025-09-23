def divide_string(string, n):
    if len(string) % n != 0:
        return "Error: String length not divisible by n."
    num_parts = len(string) // n
    parts = [string[i * n: (i + 1) * n] for i in range(num_parts)]

for char in sort:
    if char == current_char:
        count += 1
    else:
        print(f"{current_char}: {count}")
        current_char = char
        count = 1