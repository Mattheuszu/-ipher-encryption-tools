import pyperclip
from vigenere_cipher import encryptMessage as encrypt_vigenere, decryptMessage as decrypt_vigenere
from wheatstone_cipher import encryptMessage as encrypt_wheatstone, decryptMessage as decrypt_wheatstone


def main():
    print("Виберіть тип шифра:")
    print("1. Віженера (vigenere)")
    print("2. Двійний квадрат Вітстона (wheatstone)")
    cipher_choice = input("Введіть номер (1 або 2): ").strip()

    if cipher_choice == '1':
        cipher_type = 'vigenere'
    elif cipher_choice == '2':
        cipher_type = 'wheatstone'
    else:
        print("Невірний вибір шифра.")
        return

    message = input("Введіть повідомлення: ").strip()
    key = input("Введіть ключ: ").strip()

    print("\nОберіть режим:")
    print("1. Шифрування (encrypt)")
    print("2. Розшифрування (decrypt)")
    mode_choice = input("Введіть номер (1 або 2): ").strip()

    if mode_choice == '1':
        mode = 'encrypt'
    elif mode_choice == '2':
        mode = 'decrypt'
    else:
        print("Невірний режим.")
        return

    if cipher_type == 'vigenere':
        if mode == 'encrypt':
            translated = encrypt_vigenere(key, message)
        elif mode == 'decrypt':
            translated = decrypt_vigenere(key, message)
    elif cipher_type == 'wheatstone':
        if mode == 'encrypt':
            translated = encrypt_wheatstone(key, message)
        elif mode == 'decrypt':
            translated = decrypt_wheatstone(key, message)

    print(f'\nРезультат ({mode}): {translated}')
    pyperclip.copy(translated)
    print('Повідомлення було скопійовано в буфер обміну.\n')

    if mode == 'encrypt':
        if cipher_type == 'vigenere':
            decrypted = decrypt_vigenere(key, translated)
        elif cipher_type == 'wheatstone':
            decrypted = decrypt_wheatstone(key, translated)
        print(f'Дешифрування ({translated}): {decrypted}')
        print('Перевірка успішності:', 'Успіх!' if decrypted == message else 'Помилка!')


if __name__ == '__main__':
    main()
