import numpy as np
import math, string, random
import base64

def repr(M):
    for ligne in M:
        print(ligne)

def reverse(str, key):
    reverse_str = ''
    for char in reversed(str) :
        reverse_str += char
    return reverse_str

def caesar_cipher(str, key):
    chains = ["AQWZSXEDCRFVTGBYHNUJIKOLPM",
              "azeqsdwxcrtyfghvbnuiojklpm",
              '5241738906',
              "&é'(-è_çà)=~#{[|`\^@]}¨$£¤ù%*µ?,.;/:§! ê<>"
             ]
    crypted_str = ""
    for char in str :
        char_chain = ""
        for chain in chains :
            if char in chain :
                char_chain = chain
        if char_chain == "" :
            return f"Character {char} unknown."
        i = char_chain.index(char)
        char_key = (key + i) % len(char_chain)
        crypted_str += char_chain[char_key]
    return crypted_str

def caesar_cipher_decode(str, key):
    return caesar_cipher(str, -key)

def caesar_mod(str, key):
    chains = ["AQWZSXEDCRFVTGBYHNUJIKOLPM",
              "azeqsdwxcrtyfghvbnuiojklpm",
              '5241738906',
              "&é'(-è_çà)=~#{[|`\^@]}¨$£¤ù%*µ?,.;/:§! ê<>"
             ]
    crypted_str = ""
    for char in str :
        char_chain = ""
        for chain in chains :
            if char in chain :
                char_chain = chain
        if char_chain == "" :
            return f"Character {char} unknown."
        i = char_chain.index(char)
        char_key = (key + i) % len(char_chain)
        crypted_str += char_chain[char_key]
    return crypted_str

def caesar_mod_decode(str, key):
    return caesar_mod(str, -key)


def transposition_encrypt_pers(str, key):
    # personal code to finish
    n = len(str)
    q = n // key
    r = n % key
    if r == 0:
        j = 0
    else :
        j = 1
    nb_lines = q + j

    M = [['' for _ in range(key)] for _ in range(nb_lines)]
    for i in range(nb_lines):
        for j in range(key):
            M[i][j] = str[key*i + j]
    repr(M)
    crypted_str = ''
    for j in range(key):
        for i in range(nb_lines):
            crypted_str += M[i][j]
    return crypted_str

def transposition_decrypt_pers(str, key):
    # personal code to finish
    n = len(str)
    q = n // key
    r = n % key
    if r == 0:
        nb_col = q
        M = [['' for _ in range(nb_col)] for _ in range(key)]
        for i in range(key):
            for j in range(nb_col):
                # print("key", key)
                # print("i", i)
                # print("j", j)
                # print(key*i + j)
                M[i][j] = str[nb_col*i + j]
        crypted_str = ''
        for j in range(nb_col):
            for i in range(key):
                crypted_str += M[i][j]
        return crypted_str
    else :
        nb_col = q + 1

def transposition_encrypt(message, key):
    ciphertext = [''] * key

    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext)

def transposition_decrypt(message, key):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)

def base64_encode(message, key):
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message

def base64_decode(b64_message, key):
    base64_bytes = b64_message.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('utf-8')
    return message

def xor_key_generator(n_char):
    key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + "&é'(-è_çà)=~#{[|`\^@]}¨$£¤ù%*µ?,.;/:§! ê<>") for _ in range(n_char))
    return key

def xor_code(message, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(message, key)])
