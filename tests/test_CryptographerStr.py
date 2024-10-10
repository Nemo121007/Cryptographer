import pytest
from CryptographerStr import CryptographerStr


class TestCryptographerStr:
    def test_create_CryptographerStr(self):
        s = CryptographerStr("hello")
        assert s == "hello"

    def test_create_CryptographerStr_empty_string(self):
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
