class CryptographerStr(str):
    _alf = "abcdefghijklmnopqrstuvwxyz"

    def __new__(cls, value=""):
        if isinstance(value, str):
            value = value.lower()
            return super().__new__(cls, value)
        else:
            raise TypeError("unidentified type object")

    def atbash_cipher_decryption(self, alf=None):
        from .atbash_cipher import atbash_cipher_decryption
        if alf == None:
            return atbash_cipher_decryption(self, self._alf)
        else:
            return atbash_cipher_decryption(self, alf)

