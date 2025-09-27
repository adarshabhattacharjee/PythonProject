def divide_string(string, n):
    if len(string) % n != 0:
        return "Error: String length not divisible"
    
    parts = [string[i:i+n] for i in range(0, len(string), n)]

    if all(part == parts[0] for part in parts):
        return ', '.join('"' + part + '"' for part in parts)
    else:
        return "Error: Parts do not form the sequence."


