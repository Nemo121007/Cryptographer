import pytest
from CryptographerStr.cesar_cipher import cesar_cipher_decryption


class TestCesarCipherDecryption:
    def test_encryption(self):
        cipher = "hello"
        step = 1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == "ifmmp"

    def test_zero_step(self):
        cipher = "hello"
        step = 0
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == "hello"

    def test_negative_step(self):
        cipher = "hello"
        step = -1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == "gdkkn"

    def test_big_step(self):
        cipher = "xyz"
        step = 3
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == "abc"

    def test_big_step_negative(self):
        cipher = "abc"
        step = -3
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == "xyz"

    def test_decryption(self):
        cipher = "ifmmp"
        step = -1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == "hello"

    def test_decryption_encryption(self):
        cipher = "hello"
        step = 1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        result = cesar_cipher_decryption(result, -step, alf)
        assert result == "hello"

    def test_empty_string(self):
        cipher = ""
        step = 1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == ""

    def test_encryption_string(self):
        cipher = "hello world"
        step = 1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == "ifmmp xpsme"

    def test_decryption_string(self):
        cipher = "ifmmp xpsme"
        step = -1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == "hello world"

    def test_encryption_decryption_string(self):
        cipher = "hello world"
        step = 1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        result = cesar_cipher_decryption(result, -step, alf)
        assert result == "hello world"

    def test_encryption_missing_characters(self):
        cipher = "Hello, world!"
        step = 1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == "Hfmmp, xpsme!"

    def test_decryption_missing_characters(self):
        cipher = "Hfmmp, xpsme!"
        step = -1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        assert result == "Hello, world!"

    def test_encryption_decryption_missing_characters(self):
        cipher = "Hello, world!"
        step = 1
        alf = "abcdefghijklmnopqrstuvwxyz"
        result = cesar_cipher_decryption(cipher, step, alf)
        result = cesar_cipher_decryption(result, -step, alf)
        assert result == "Hello, world!"