from CryptographerStr import CryptographerStr
def vigenere_cipher_encryption(self, key, alf):
    _check_arguments(self, key, alf)

    line = ""

    # Создание таблицы Виженера (alfCode)
    alf_code = [[alf[(i + j) % len(alf)] for j in range(len(alf))] for i in range(len(alf))]

    # Увеличение ключа до длины строки
    key_length = len(key)
    while len(key) < len(self):
        key += key[len(key) % key_length]

    # Шифрование строки
    for k, char in enumerate(self):
        for i, row_char in enumerate(alf):
            if alf_code[i][0] == key[k]:  # Находим строку с символом ключа
                for j, col_char in enumerate(alf):
                    if alf_code[0][j] == char:  # Находим столбец с символом строки
                        line += alf_code[i][j]  # Шифрованный символ
                        break
                break

    return CryptographerStr(line)


def vigenere_cipher_decryption(self, key, alf):
    _check_arguments(self, key, alf)

    line = ""

    # Создание таблицы Виженера (alfCode)
    alf_code = [[alf[(i + j) % len(alf)] for j in range(len(alf))] for i in range(len(alf))]

    # Увеличение ключа до длины строки
    key_length = len(key)
    while len(key) < len(self):
        key += key[len(key) % key_length]

    # Расшифровка строки
    for k, char in enumerate(self):
        for i, row_char in enumerate(alf):
            if alf_code[i][0] == key[k]:  # Находим строку с символом ключа
                for j, enc_char in enumerate(alf):
                    if alf_code[i][j] == char:  # Находим символ шифра
                        line += alf_code[0][j]  # Оригинальный символ
                        break
                break

    return CryptographerStr(line)

def _check_arguments(str, key, alf):
    if key == "":
        raise ValueError("Empty key")
    for symbol in str:
        if not (symbol in alf):
            raise ValueError("Symbol in string is missing from the alphabet")
    for symbol in key:
        if not (symbol in alf):
            raise ValueError("Symbol in key is missing from the alphabet")
