class CryptographerStr(str):
    _alf = "abcdefghijklmnopqrstuvwxyz"

    def __new__(cls, value=""):
        value = value.lower()
        return super().__new__(cls, value)

    def atbash_cipher_decryption(self, alf=None):
        from .atbash_cipher import atbash_cipher_decryption
        if alf == None:
            return atbash_cipher_decryption(self, self._alf)
        else:
            return atbash_cipher_decryption(self, alf)

