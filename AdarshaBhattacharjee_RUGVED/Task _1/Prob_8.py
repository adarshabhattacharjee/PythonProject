def divide_string(string, n):
    if len(string) % n != 0:
        return "Error: String length not divisible"
    num_parts = len(string) // n
    parts = [string[i * n: (i + 1) * n] for i in range(num_parts)]

    # Check if all parts are the same sequence
    if all(part == parts[0] for part in parts):
        return ', '.join('"' + part + '"' for part in parts)
    else:
        return "Error: Parts do not form the sequence."


