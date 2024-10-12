import pytest
from CryptographerStr import CryptographerStr


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

    # region тестирование декораторов
    # region тестирование методов Атбаш
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
        def mock_atbash_cipher_decryption(input_str, alf):
            assert input_str == "hello"
            assert alf == "abcdefghijklmnopqrstuvwxyz"
            return "mocked_result"

        monkeypatch.setattr('CryptographerStr.atbash_cipher.atbash_cipher_decryption', mock_atbash_cipher_decryption)

        s = CryptographerStr("hello")

        result = s.atbash_cipher_decryption()
        assert result == "mocked_result"

    def test_atbash_cipher_decryption_alf(self, monkeypatch):
        def mock_atbash_cipher_decryption(input_str, alf):
            assert input_str == "hello"
            assert alf == "abc"
            return "mocked_result"

        monkeypatch.setattr('CryptographerStr.atbash_cipher.atbash_cipher_decryption', mock_atbash_cipher_decryption)

        s = CryptographerStr("hello")

        result = s.atbash_cipher_decryption("abc")
        assert result == "mocked_result"

    def test_atbash_cipher_decryption_raises_type_error_for_invalid_self(self):
        non_str_instance = 123

        with pytest.raises(TypeError, match="unidentified type object in str"):
            CryptographerStr.atbash_cipher_decryption(non_str_instance)

    def test_atbash_unidentified_object_in_alf(self):
        with pytest.raises(TypeError, match="unidentified type object in alf"):
            s = (CryptographerStr("hello")).atbash_cipher_decryption(123)
    # endregion

    # region шифр цезаря
    def test_cesar_cipher_decryption_string(self, monkeypatch):
        # Создаем фиктивную функцию для имитации вызова
        def mock_cesar_cipher_decryption(input_str, step, alf):
            assert input_str == "hello"
            return "mocked_result"

        # Используем pytest monkeypatch для замены реальной функции на фиктивную
        monkeypatch.setattr('CryptographerStr.cesar_cipher.cesar_cipher_decryption', mock_cesar_cipher_decryption)

        s = CryptographerStr("hello")

        # Проверяем результат вызова метода
        result = s.cesar_cipher_decryption()
        assert result == "mocked_result"

    def test_cesar_cipher_decryption_empty_alf(self, monkeypatch):
        def mock_cesar_cipher_decryption(input_str, step, alf):
            assert alf == "abcdefghijklmnopqrstuvwxyz"
            return "mocked_result"

        monkeypatch.setattr('CryptographerStr.cesar_cipher.cesar_cipher_decryption', mock_cesar_cipher_decryption)

        s = CryptographerStr()

        result = s.cesar_cipher_decryption()
        assert result == "mocked_result"

    def test_cesar_cipher_decryption_empty_step(self, monkeypatch):
        def mock_cesar_cipher_decryption(input_str, step, alf):
            assert step == 1
            return "mocked_result"

        monkeypatch.setattr('CryptographerStr.cesar_cipher.cesar_cipher_decryption', mock_cesar_cipher_decryption)

        s = CryptographerStr()

        result = s.cesar_cipher_decryption()
        assert result == "mocked_result"

    def test_cesar_cipher_decryption_string_and_alf_and_step(self, monkeypatch):
        def mock_cesar_cipher_decryption(input_str, step, alf):
            assert input_str == "hello"
            assert step == 5
            assert alf == "abcdefghijklmnopqrstuvwxyz"
            return "mocked_result"

        monkeypatch.setattr('CryptographerStr.cesar_cipher.cesar_cipher_decryption', mock_cesar_cipher_decryption)

        s = CryptographerStr("hello")

        result = s.cesar_cipher_decryption(5)
        assert result == "mocked_result"

    def test_cesar_cipher_decryption_alf(self, monkeypatch):
        def mock_cesar_cipher_decryption(input_str, step, alf):
            assert input_str == "hello"
            assert step == 5
            assert alf == "abc"
            return "mocked_result"

        monkeypatch.setattr('CryptographerStr.cesar_cipher.cesar_cipher_decryption', mock_cesar_cipher_decryption)

        s = CryptographerStr("hello")

        result = s.cesar_cipher_decryption(5, "abc")
        assert result == "mocked_result"

    def test_cesar_cipher_decryption_raises_type_error_for_invalid_self(self):
        non_str_instance = 123

        with pytest.raises(TypeError, match="unidentified type object in str"):
            CryptographerStr.cesar_cipher_decryption(non_str_instance)

    def test_cesar_unidentified_object_in_step(self):
        with pytest.raises(TypeError, match="unidentified type object in step"):
            s = (CryptographerStr("hello")).cesar_cipher_decryption([])

    def test_cesar_unidentified_object_in_step_float(self):
        with pytest.raises(TypeError, match="unidentified type object in step"):
            s = (CryptographerStr("hello")).cesar_cipher_decryption(1.5)

    def test_cesar_unidentified_object_in_alf(self):
        with pytest.raises(TypeError, match="unidentified type object in alf"):
            s = (CryptographerStr("hello")).cesar_cipher_decryption(1, [])
    # endregion шифр цезаря

    # region Шифр Вижинера
    # region Шифрование
    def test_vigenere_cipher_encryption_string_key_alf(self, monkeypatch):
        # Создаем фиктивную функцию для имитации вызова
        def mock_vigenere_cipher_encryption(input_str, key, alf):
            assert input_str == "hello"
            assert key == "world"
            assert alf == "abcdefghijklmnopqrstuvwxyz"
            return "mocked_result"

        # Используем pytest monkeypatch для замены реальной функции на фиктивную
        monkeypatch.setattr('CryptographerStr.vigenere_cipher.vigenere_cipher_encryption',
                            mock_vigenere_cipher_encryption)

        s = CryptographerStr("hello")

        # Проверяем результат вызова метода
        result = s.vigenere_cipher_encryption("world", "abcdefghijklmnopqrstuvwxyz")
        assert result == "mocked_result"

    def test_vigenere_cipher_encryption_string_key_empty_alf(self, monkeypatch):
        # Создаем фиктивную функцию для имитации вызова
        def mock_vigenere_cipher_encryption(input_str, key, alf):
            assert input_str == "hello"
            assert key == "world"
            assert alf == "abcdefghijklmnopqrstuvwxyz"
            return "mocked_result"

        # Используем pytest monkeypatch для замены реальной функции на фиктивную
        monkeypatch.setattr('CryptographerStr.vigenere_cipher.vigenere_cipher_encryption',
                            mock_vigenere_cipher_encryption)

        s = CryptographerStr("hello")

        # Проверяем результат вызова метода
        result = s.vigenere_cipher_encryption("world")
        assert result == "mocked_result"

    def test_vigenere_cipher_encryption_invalid_self(self):
        non_str_instance = 123

        with pytest.raises(TypeError, match="unidentified type object in str"):
            CryptographerStr.vigenere_cipher_encryption(non_str_instance, "world")

    def test_vigenere_cipher_encryption_invalide_key(self):
        with pytest.raises(TypeError, match="unidentified type object in key"):
            s = (CryptographerStr("hello")).vigenere_cipher_encryption([])

    def test_vigenere_cipher_encryption_invalide_alf(self):
        with pytest.raises(TypeError, match="unidentified type object in alf"):
            s = (CryptographerStr("hello")).vigenere_cipher_encryption("world", [])
    # endregion

    # region Дешифрование
    def test_vigenere_cipher_decryption_string_key_alf(self, monkeypatch):
        # Создаем фиктивную функцию для имитации вызова
        def mock_vigenere_cipher_decryption(input_str, key, alf):
            assert input_str == "hello"
            assert key == "world"
            assert alf == "abcdefghijklmnopqrstuvwxyz"
            return "mocked_result"

        # Используем pytest monkeypatch для замены реальной функции на фиктивную
        monkeypatch.setattr('CryptographerStr.vigenere_cipher.vigenere_cipher_decryption',
                            mock_vigenere_cipher_decryption)

        s = CryptographerStr("hello")

        # Проверяем результат вызова метода
        result = s.vigenere_cipher_decryption("world", "abcdefghijklmnopqrstuvwxyz")
        assert result == "mocked_result"

    def test_vigenere_cipher_decryption_string_key_empty_alf(self, monkeypatch):
        # Создаем фиктивную функцию для имитации вызова
        def mock_vigenere_cipher_decryption(input_str, key, alf):
            assert input_str == "hello"
            assert key == "world"
            assert alf == "abcdefghijklmnopqrstuvwxyz"
            return "mocked_result"

        # Используем pytest monkeypatch для замены реальной функции на фиктивную
        monkeypatch.setattr('CryptographerStr.vigenere_cipher.vigenere_cipher_decryption',
                            mock_vigenere_cipher_decryption)

        s = CryptographerStr("hello")

        # Проверяем результат вызова метода
        result = s.vigenere_cipher_decryption("world")
        assert result == "mocked_result"

    def test_vigenere_cipher_decryption_invalid_self(self):
        non_str_instance = 123

        with pytest.raises(TypeError, match="unidentified type object in str"):
            CryptographerStr.vigenere_cipher_decryption(non_str_instance, "world")

    def test_vigenere_cipher_decryption_invalide_key(self):
        with pytest.raises(TypeError, match="unidentified type object in key"):
            s = (CryptographerStr("hello")).vigenere_cipher_decryption([])

    def test_vigenere_cipher_decryption_invalide_alf(self):
        with pytest.raises(TypeError, match="unidentified type object in alf"):
            s = (CryptographerStr("hello")).vigenere_cipher_decryption("world", [])
    # endregion
    # endregion
    # endregion
