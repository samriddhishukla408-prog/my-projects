def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char
    return result
 
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
 
message = input("Enter a message: ")
shift_value = int(input("Enter shift value : "))
 
encrypted = caesar_encrypt(message, shift_value)
print("Encrypted:", encrypted)
 
decrypted = caesar_decrypt(encrypted, shift_value)
print("Decrypted back:", decrypted)