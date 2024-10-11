import pytest
from CryptographerStr.atbash_cipher import atbash_cipher_decryption


class TestAtbashCipherDecryption:
    def test_encryption(self):
        cipher = "Hello"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "Hvool"

    def test_decryption(self):
        cipher = "Hvool"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "Hello"

    def test_decryption_encryption(self):
        cipher = "Hello"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        result = atbash_cipher_decryption(result, alf)
        assert result == "Hello"

    def test_empty_string(self):
        cipher = ""
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == ""

    def test_encryption_string(self):
        cipher = "Hello world"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "Hvool dliow"

    def test_decryption_string(self):
        cipher = "Hvool dliow"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "Hello world"

    def test_encryption_decryption_string(self):
        cipher = "Hello world"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        result = atbash_cipher_decryption(result, alf)
        assert result == "Hello world"

    def test_encryption_one_char_1(self):
        cipher = "a"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "z"

    def test_encryption_one_char_2(self):
        cipher = "c"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "x"

    def test_encryption_one_char_3(self):
        cipher = "n"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "m"

    def test_encryption_one_char_4(self):
        cipher = "m"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        result = atbash_cipher_decryption(result, alf)
        assert result == "m"

    def test_encryption_missing_characters(self):
        cipher = "Hello, world!"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "Hvool, dliow!"

    def test_decryption_missing_characters(self):
        cipher = "Hvool, dliow!"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "Hello, world!"

    def test_encryption_decryption_missing_characters(self):
        cipher = "Hello, world!"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        result = atbash_cipher_decryption(result, alf)
        assert result == "Hello, world!"
