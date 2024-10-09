import pytest
from CryptographerStr.atbash_cipher import atbash_cipher_decryption


class TestAtbashCipherDecryption:
    def test_simple_decryption(self):
        cipher = "Hvool, Wliow!"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "Hello, World!"

    def test_non_alphabet_chars(self):
        cipher = "Hello, World!"
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "Hvool, Wliow!"

    def test_empty_string(self):
        cipher = ""
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == ""

    def test_repeated_chars(self):
        cipher = "aaaa"
        alf = "abcd"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "dddd"

    def test_custom_alphabet(self):
        cipher = "XYZ"
        alf = "ZYX"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "ZYX"

    def test_non_ascii_chars(self):
        cipher = "Привет, мир!"
        alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        result = atbash_cipher_decryption(cipher, alf)
        assert result == "Поцэъм, тцо!"
