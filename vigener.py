def vigenere(M, key):
    indice_key = 0
    message_code = ""

    for i in range(0, len(M)):
        if 'A' <= M[i] <= 'Z':
            message_code += chr((((ord(M[i]) - ord('A')) + (ord(key[indice_key]) - ord('A'))) % 26) + ord('A'))
            indice_key = (indice_key + 1) % len(key)
        else:
            message_code += M[i]
    return message_code


def decode_vigenere(M, key):
    indice_key = 0
    message_code = ""

    for i in range(0, len(M)):
        if 'A' <= M[i] <= 'Z':
            message_code += chr((((ord(M[i]) - ord('A')) - (ord(key[indice_key]) - ord('A'))) % 26) + ord('A'))
            indice_key = (indice_key + 1) % len(key)
        else:
            message_code += M[i]
    return message_code


print(vigenere('BILAL EL MANNOUTI', 'PYTHON'))
print(decode_vigenere('F8dmeMlB+TyOSKZvcl1sVV8ZikqGUZZqSDxwH/80qKI=', 'microsoc'))

