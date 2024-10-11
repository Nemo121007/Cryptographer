import pytest
from CryptographerStr import CryptographerStr, atbash_cipher
from CryptographerStr.atbash_cipher import atbash_cipher_decryption


class TestCryptographerStr:
    # region Тестирование конструктора
    def test_create_cryptographer_str(self):
        s = CryptographerStr("hello")
        assert s == "hello"

    def test_create_cryptographe_str_empty_string(self):
        s = CryptographerStr()
        assert s == ""

    def test_lower_case(self):
        s = CryptographerStr("HeLlO")
        assert s == "hello"

    def test_unusual_symbols(self):
        s = CryptographerStr("123!@#")
        assert s == "123!@#"

    def test_string_many_world(self):
        s = CryptographerStr("hello world")
        assert s == "hello world"

    def test_non_english_characters(self):
        s = CryptographerStr("привет мир")
        assert s == "привет мир"

    def test_multi_line_string(self):
        s = CryptographerStr("hello\nworld")
        assert s == "hello\nworld"

    def test_combine_constructor(self):
        s = CryptographerStr("HeLlO\nмИр!")
        assert s == "hello\nмир!"

    def test_unidentified_object(self):
        with pytest.raises(TypeError, match="unidentified type object"):
            s = CryptographerStr([])

    # endregion

    # region тестирование методов
    def test_atbash_cipher_decryption_string(self, monkeypatch):
        # Создаем фиктивную функцию для имитации вызова
        def mock_atbash_cipher_decryption(input_str, alf):
            assert input_str == "hello"
            return "mocked_result"

        # Используем pytest monkeypatch для замены реальной функции на фиктивную
        monkeypatch.setattr('CryptographerStr.atbash_cipher.atbash_cipher_decryption', mock_atbash_cipher_decryption)

        s = CryptographerStr("hello")

        # Проверяем результат вызова метода
        result = s.atbash_cipher_decryption()
        assert result == "mocked_result"

    def test_atbash_cipher_decryption_empty_alf(self, monkeypatch):
        def mock_atbash_cipher_decryption(input_str, alf):
            assert alf == "abcdefghijklmnopqrstuvwxyz"
            return "mocked_result"

        monkeypatch.setattr('CryptographerStr.atbash_cipher.atbash_cipher_decryption', mock_atbash_cipher_decryption)

        s = CryptographerStr()

        result = s.atbash_cipher_decryption()
        assert result == "mocked_result"

    def test_atbash_cipher_decryption_string_and_alf(self, monkeypatch):
        # Создаем фиктивную функцию для имитации вызова
        def mock_atbash_cipher_decryption(input_str, alf):
            assert input_str == "hello"
            assert alf == "abcdefghijklmnopqrstuvwxyz"
            return "mocked_result"

        # Используем pytest monkeypatch для замены реальной функции на фиктивную
        monkeypatch.setattr('CryptographerStr.atbash_cipher.atbash_cipher_decryption', mock_atbash_cipher_decryption)

        s = CryptographerStr("hello")

        # Проверяем результат вызова метода
        result = s.atbash_cipher_decryption()
        assert result == "mocked_result"

    def test_atbash_cipher_decryption_alf(self, monkeypatch):
        # Создаем фиктивную функцию для имитации вызова
        def mock_atbash_cipher_decryption(input_str, alf):
            assert input_str == "hello"
            assert alf == "abc"
            return "mocked_result"

        # Используем pytest monkeypatch для замены реальной функции на фиктивную
        monkeypatch.setattr('CryptographerStr.atbash_cipher.atbash_cipher_decryption', mock_atbash_cipher_decryption)

        s = CryptographerStr("hello")

        # Проверяем результат вызова метода
        result = s.atbash_cipher_decryption("abc")
        assert result == "mocked_result"

    # endregion
