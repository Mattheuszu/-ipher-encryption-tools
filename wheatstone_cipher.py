def create_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    table = key + ''.join([char for char in alphabet if char not in key])
    return table

def encryptMessage(key, message):
    table = create_table(key.upper())
    message = ''.join([char.upper() for char in message if char.upper() in table])
    cipher = ""
    for i in range(0, len(message), 2):
        if i + 1 < len(message):
            row1 = table.index(message[i]) // 5
            col1 = table.index(message[i]) % 5
            row2 = table.index(message[i + 1]) // 5
            col2 = table.index(message[i + 1]) % 5
            if row1 == row2:
                cipher += table[row1 * 5 + (col1 + 1) % 5]
                cipher += table[row2 * 5 + (col2 + 1) % 5]
            elif col1 == col2:
                cipher += table[((row1 + 1) % 5) * 5 + col1]
                cipher += table[((row2 + 1) % 5) * 5 + col2]
            else:
                cipher += table[row1 * 5 + col2]
                cipher += table[row2 * 5 + col1]
        else:
            cipher += message[i]
    return cipher

def decryptMessage(key, message):
    table = create_table(key.upper())
    message = ''.join([char.upper() for char in message if char.upper() in table])
    plain = ""
    for i in range(0, len(message), 2):
        if i + 1 < len(message):
            row1 = table.index(message[i]) // 5
            col1 = table.index(message[i]) % 5
            row2 = table.index(message[i + 1]) // 5
            col2 = table.index(message[i + 1]) % 5
            if row1 == row2:
                plain += table[row1 * 5 + (col1 - 1) % 5]
                plain += table[row2 * 5 + (col2 - 1) % 5]
            elif col1 == col2:
                plain += table[((row1 - 1) % 5) * 5 + col1]
                plain += table[((row2 - 1) % 5) * 5 + col2]
            else:
                plain += table[row1 * 5 + col2]
                plain += table[row2 * 5 + col1]
        else:
            plain += message[i]
    return plain
