import math

# Caeser Encrypt
def caesar_cipher(text, shift, space_char, non_alpha_char):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + int(shift)) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + int(shift)) % 26 + 97)
        elif char.isdigit():
            new_digit = (int(char) + shift) % 10
            result += str(new_digit)
        elif char.isspace():
            result += space_char
        else:
            result += non_alpha_char

    return result

# Caeser Decrypt
def reverse_caesar_cipher(text, shift, space_char, non_alpha_char, blank_space):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + int(shift)) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + int(shift)) % 26 + 97)
        elif char.isdigit():
            new_digit = (int(char) + shift) % 10
            result += str(new_digit)
        elif char == non_alpha_char:
            result += space_char
        elif char == space_char:
            result += blank_space

    return result

# Transposition Encrypt
def encryptMessage(msg):
    cipher = ""
  
    # track key indices
    k_indx = 0
  
    msg_len = float(len(msg))    # Obtain the length of the msg from user
    msg_lst = list(msg)          # Define number to all the char in the msg, example: Jason -> "J", "a", "s", "o", "n"
    key_lst = sorted(list(key))  # Sort the accending order of the msg, example: Jason -> 21543
  
    # calculate column of the matrix
    col = len(key)
      
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
  
    # add the padding character '_' in empty
    # the empty cell of the matix 
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
  
    # create Matrix and insert message and 
    # padding characters row-wise 
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
  
    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] 
                          for row in matrix])
        k_indx += 1
  
    return cipher

# Transposition Decrypt
def decryptMessage(cipher):
    msg = ""
  
    # track key indices
    k_indx = 0
  
    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
  
    # calculate column of the matrix
    col = len(key)
      
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
  
    # convert key into list and sort 
    # alphabetically so we can access 
    # each character by its alphabetical position.
    key_lst = sorted(list(key))
  
    # create an empty matrix to 
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
  
    # Arrange the matrix column wise according 
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
  
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
  
    # convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
  
    null_count = msg.count('_')
  
    if null_count > 0:
        return msg[: -null_count]
  
    return msg

# Driver Code
space_char = "-"
non_alpha_char = "?"
blank_space = " "

print("Enter your message:")   
msg = input()

print("Enter number of shift:")
shift = input()

print("Enter your key:")
key = input()

print("Original Test: {}".format(msg))

encrypted_text = encryptMessage(caesar_cipher(msg, shift, space_char, non_alpha_char))


print("Encrypted Message: {}".format((encrypted_text)))

decrypted_text = reverse_caesar_cipher(decryptMessage(encrypted_text), -int(shift), space_char, non_alpha_char, blank_space)

print("Decryped Message: {}".format((decrypted_text)))

