alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


class CryptographerStr(str):
    def __new__(cls, value):
        return super().__new__(cls, value.lower)

    def atbash_cipher_decryption(self):
        from atbash_cipher import atbash_cipher_decryption
        return atbash_cipher_decryption(self, alf)
