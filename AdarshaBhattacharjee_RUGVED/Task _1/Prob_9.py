
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        encrypted_char = chr((ord(char)  + shift)  )
        result += encrypted_char


    return result
