import pytest
from CryptographerStr.vigenere_cipher import vigenere_cipher_decryption, vigenere_cipher_encryption

class TestVigenereCipherDecryption:
    def test_encryption(self):
        cipher = "hello"
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = vigenere_cipher_encryption(cipher, key, alf)
        assert result == "dscwr"

    def test_decryption(self):
        cipher = "dscwr"
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = vigenere_cipher_decryption(cipher, key, alf)
        assert result == "hello"

    def test_decryption_invalide_key(self):
        cipher = "dscwr"
        key = "word"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = vigenere_cipher_decryption(cipher, key, alf)
        assert result != "hello"

    def test_decryption_encryption(self):
        cipher = "hello"
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = vigenere_cipher_encryption(cipher, key, alf)
        result = vigenere_cipher_decryption(result, key, alf)
        assert result == "hello"

    def test_encryption_empty_string(self):
        cipher = ""
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = vigenere_cipher_encryption(cipher, key, alf)
        assert result == ""

    def test_decryption_empty_string(self):
        cipher = ""
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = vigenere_cipher_decryption(cipher, key, alf)
        assert result == ""

    def test_encryption_string(self):
        cipher = "hello world"
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz "
        result = vigenere_cipher_encryption(cipher, key, alf)
        assert result == "csbwrvjeboz"

    def test_decryption_string(self):
        cipher = "csbwrvjeboz"
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz "
        result = vigenere_cipher_decryption(cipher, key, alf)
        assert result == "hello world"

    def test_encryption_decryption_string(self):
        cipher = "hello world"
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz "
        result = vigenere_cipher_encryption(cipher, key, alf)
        result = vigenere_cipher_decryption(result, key, alf)
        assert result == "hello world"

    def test_encryption_one_symbol(self):
        cipher = "a"
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz "
        result = vigenere_cipher_encryption(cipher, key, alf)
        assert result == "w"

    def test_decryption_one_symbol(self):
        cipher = "w"
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz "
        result = vigenere_cipher_decryption(cipher, key, alf)
        assert result == "a"

    def test_encryption_decryption_one_symbol(self):
        cipher = "a"
        key = "world"
        alf = "abcdefghijklmnopqrstuvwxyz "
        result = vigenere_cipher_encryption(cipher, key, alf)
        result = vigenere_cipher_decryption(result, key, alf)
        assert result == "a"

    def test_encryption_different_keys(self):
        cipher = "hello"
        key_1 = "world"
        alf = "abcdefghijklmnopqrstuvwxyz "
        result_1 = vigenere_cipher_encryption(cipher, key_1, alf)
        key_2 = "word"
        result_2 = vigenere_cipher_encryption(cipher, key_2, alf)
        assert result_1 != result_2

    def test_decryption_different_keys(self):
        cipher = "hello"
        key_1 = "world"
        alf = "abcdefghijklmnopqrstuvwxyz "
        result_1 = vigenere_cipher_decryption(cipher, key_1, alf)
        key_2 = "word"
        result_2 = vigenere_cipher_decryption(cipher, key_2, alf)
        assert result_1 != result_2

    def test_encryption_string_equal_key(self):
        cipher = "world"
        key_1 = "world"
        key_2 = "world"
        alf = "abcdefghijklmnopqrstuvwxyz "
        result_1 = vigenere_cipher_encryption(cipher, key_1, alf)
        result_2 = vigenere_cipher_encryption(cipher, key_2, alf)
        assert result_1 == result_2

    def test_decryption_string_equal_key(self):
        cipher = "rbhwg"
        key_1 = "world"
        key_2 = "world"
        alf = "abcdefghijklmnopqrstuvwxyz "
        result_1 = vigenere_cipher_decryption(cipher, key_1, alf)
        result_2 = vigenere_cipher_decryption(cipher, key_2, alf)
        assert result_1 == result_2

    def test_encryption_missing_characters(self):
        with pytest.raises(ValueError, match="Symbol in string is missing from the alphabet"):
            s = vigenere_cipher_encryption("hello!>", "world","hijklmno")

    def test_decryption_missing_characters(self):
        with pytest.raises(ValueError, match="Symbol in string is missing from the alphabet"):
            s = vigenere_cipher_decryption("hello!>", "world","hijklmno")

    def test_encryption_missing_characters_in_key(self):
        with pytest.raises(ValueError, match="Symbol in key is missing from the alphabet"):
            s = vigenere_cipher_encryption("hl", "world","hijklmno")

    def test_decryption_missing_characters_in_key(self):
        with pytest.raises(ValueError, match="Symbol in key is missing from the alphabet"):
            s = vigenere_cipher_decryption("hl", "world","hijklmno")

    def test_encryption_empty_key(self):
        with pytest.raises(ValueError, match="Empty key"):
            s = vigenere_cipher_encryption("hello", "","abcdefghijklmnopqrstuvwxyz")

    def test_decryption_empty_key(self):
        with pytest.raises(ValueError, match="Empty key"):
            s = vigenere_cipher_decryption("hello", "","abcdefghijklmnopqrstuvwxyz")

