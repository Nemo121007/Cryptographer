def atbash_cipher_decryption(self, alf):
    result = ""
    for char in self:
        if char in alf:
            index = alf.index(char)
            result += alf[len(alf) - index - 1]
        else:
            result += char  # Если символ не найден в алфавите, добавляем его как есть
    return result


if __name__ == "__main__":
    decryption_string = "пример"
    print(decryption_string)
    encryption_string = atbash_cipher_decryption(decryption_string, "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    print(encryption_string)
    decryption_string = atbash_cipher_decryption(encryption_string, "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    print(decryption_string)
