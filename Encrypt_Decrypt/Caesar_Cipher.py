def caesar_cipher(text, shift, space_char, non_alpha_char):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isdigit():
            new_digit = (int(char) + shift) % 10
            result += str(new_digit)
        elif char.isspace():
            result += space_char
        else:
            result += non_alpha_char

    return result

def reverse_caesar_cipher(text, shift, space_char, non_alpha_char, blank_space):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isdigit():
            new_digit = (int(char) + shift) % 10
            result += str(new_digit)
        elif char == non_alpha_char:
            result += space_char
        elif char == space_char:
            result += blank_space

    return result

# Example usage
plain_text = "Hello, world! 123"
shift = 3
space_char = "-"
non_alpha_char = "?"
blank_space = " "

encrypted_text = caesar_cipher(plain_text, shift, space_char, non_alpha_char)
print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)

decrypted_text = reverse_caesar_cipher(encrypted_text, -shift, space_char, non_alpha_char, blank_space)
print("Decrypted Text:", decrypted_text)
