class CryptographerStr(str):
    _alf = "abcdefghijklmnopqrstuvwxyz"

    def __new__(cls, value=""):
        if isinstance(value, str):
            value = value.lower()
            return super().__new__(cls, value)
        else:
            raise TypeError("unidentified type object")

    def atbash_cipher_decryption(self, alf=None):
        if not isinstance(self, str):
            raise TypeError("unidentified type object in str")
        if not isinstance(alf, str) and alf is not None:
            raise TypeError("unidentified type object in alf")
        from .atbash_cipher import atbash_cipher_decryption
        if alf is None:
            return atbash_cipher_decryption(self, self._alf)
        else:
            return atbash_cipher_decryption(self, alf)

    def cesar_cipher_decryption(self, step=1, alf=None):
        if not isinstance(self, str):
            raise TypeError("unidentified type object in str")
        if not isinstance(step, int):
            raise TypeError("unidentified type object in step")
        if not isinstance(alf, str) and alf is not None:
            raise TypeError("unidentified type object in alf")
        from .cesar_cipher import cesar_cipher_decryption
        if alf is None:
            return cesar_cipher_decryption(self, step, self._alf)
        else:
            return cesar_cipher_decryption(self, step, alf)
