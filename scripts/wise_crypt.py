from cryptalgo import *
import random

list_algo = [(reverse, reverse),
             (caesar_cipher, caesar_cipher_decode),
             (caesar_mod, caesar_mod_decode),
             (transposition_encrypt, transposition_decrypt),
             # the 2 lasts
             (xor_code, xor_code),
             (base64_encode, base64_decode)
              ]

def keys_generator(i, str):
    if i == 0:
        return None
    if i == 1:
        return random.randint(0, 42)
    if i == 2:
        return random.randint(0, 10**1000)
    if i == 3:
        return random.randint(1, len(str))
    if i == -2:
        return xor_key_generator(len(str) + 1024)
    if i == -1:
        return None


def structure_generator(n_layers, str):
    n_algo = len(list_algo[:2])
    q = n_layers // n_algo
    r = n_layers % n_algo
    algo_list = []
    for _ in range(q):
        algo_list += random.sample(range(0, n_algo), n_algo)
    algo_list += random.sample(range(0, n_algo), r)
    random.shuffle(algo_list)

    structure = []
    for i in algo_list:
        structure.append([list_algo[i], keys_generator(i, str)])

    # The 2 lasts layers
    structure.append([list_algo[-2], keys_generator(-2, str)])
    structure.append([list_algo[-1], keys_generator(-1, str)])

    return structure

def encode(message, n_layers):
    structure = structure_generator(n_layers, message)
    print(message)
    for layer in structure:
        message = layer[0][0](message, layer[1])
        print(message)
    return message, structure

def decode(message, structure):
    for layer in reversed(structure):
        message = layer[0][1](message, layer[1])
    return message

# Final functions
def wise_encode(message, n_layers):
    structure = structure_generator(n_layers, message)
    for layer in structure:
        message = layer[0][0](message, layer[1])
        print(message)
    return message, structure

def wise_decode(message, structure):
    for layer in reversed(structure):
        message = layer[0][1](message, layer[1])
        print(message)
    return message

print('Bonjour')
encode, structure = wise_encode("Bonjour", 10)

print("\ndecode")
decode = wise_decode(encode, structure)
