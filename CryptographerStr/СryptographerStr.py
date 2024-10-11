class CryptographerStr(str):
    _alf = "abcdefghijklmnopqrstuvwxyz"

    def __new__(cls, value=""):
        value = value.lower()
        return super().__new__(cls, value)

    def atbash_cipher_decryption(self):
        from atbash_cipher import atbash_cipher_decryption
        return atbash_cipher_decryption(self, self._alf)
