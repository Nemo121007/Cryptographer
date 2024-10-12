import pytest
from CryptographerStr import CryptographerStr

class TestIntegration:
    def test_atbash_cipher_decryption(self):
        s = CryptographerStr("hello")
        result = s.atbash_cipher_decryption()
        assert result == "svool"

    def test_atbash_cipher_encryption_decryption(self):
        s = CryptographerStr("hello")
        s = s.atbash_cipher_decryption()
        assert s == "svool"
        result = s.atbash_cipher_decryption()
        assert result == "hello"

    def test_cesar_cipher_decryption(self):
        s = CryptographerStr("hello")
        result = s.cesar_cipher_decryption()
        assert result == "ifmmp"

    def test_cesar_cipher_encryption_decryption(self):
        s = CryptographerStr("hello")
        s = s.cesar_cipher_decryption(1)
        assert s == "ifmmp"
        result = s.cesar_cipher_decryption(-1)
        assert result == "hello"

    def test_vigenere_cipher_encryption(self):
        s = CryptographerStr("hello")
        result = s.vigenere_cipher_encryption("world")
        assert result == "dscwr"

    def test_vigenere_cipher_encryption_deep_error(self):
        with pytest.raises(ValueError, match="Empty key"):
            s = CryptographerStr("hello").vigenere_cipher_encryption("")

    def test_vigenere_cipher_decryption(self):
        s = CryptographerStr("hello")
        result = s.vigenere_cipher_decryption("world")
        assert result == "lqual"

    def test_vigenere_cipher_decryption_deep_error(self):
        with pytest.raises(ValueError, match="Empty key"):
            s = CryptographerStr("hello").vigenere_cipher_decryption("")

    def test_vigenere_cipher_encryption_decryption(self):
        s = CryptographerStr("hello")
        s = s.vigenere_cipher_encryption("world")
        assert s == "dscwr"
        result = s.vigenere_cipher_decryption("world")
        assert result == "hello"
