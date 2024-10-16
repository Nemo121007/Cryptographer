# Модульные тесты класса
#### Тест М1.1: Создание класса из строки(test_create_CryptographerStr)
*Тип теста:* Позитивный
*Описание:* Проверка создания класса из строки

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

*Входные данные:* "hello"

*Ожидаемый результат:* "hello"
#### Тест М1.2: Создание класса без аргументов (test_create_CryptographerStr_empty_string)
*Тип теста:* Позитивный

*Описание:* Проверка создания класса без аргументов

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

*Входные данные:* отсутствуют

*Ожидаемый результат:* ""
#### Тест М1.3: Перевод строки в нижний регистр (test_lower_case)
*Тип теста:* Позитивный

*Описание:* Проверка перевода строки в нижний регистр при создании класса

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

*Входные данные:* "HeLlO"

*Ожидаемый результат:* "hello"
#### Тест М1.4: Обработка нетекстовых символов (test_unusual_symbols)
*Тип теста:* Позитивный

*Описание:* Проверка обработки нетекстовых символов при создании класса

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

*Входные данные:* "123!@#"

*Ожидаемый результат:* "123!@#"
#### Тест М1.5: Создание класса из строки, состоящей из нескольких слов (test_string_many_world)
*Тип теста:* Позитивный

*Описание:* Проверка создания класса из строки, содержащей несколько слов (разделитель - пробел)

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

*Входные данные:* "hello world"

*Ожидаемый результат:* "hello world"
#### Тест М1.6: Создание класса из неанглоязычной строки (test_non_english_characters)
*Тип теста:* Позитивный

*Описание:* Проверка создания класса из неанглоязычной строки

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

*Входные данные:* "привет мир"

*Ожидаемый результат:* "привет мир"
#### Тест М1.7: Создание класса из строки, содержащей символы переноса строки (test_multi_line_string)
*Тип теста:* Позитивный

*Описание:* Проверка создания класса из строки, содержащей символы переноса строки

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

*Входные данные:* "hello\nworld"

*Ожидаемый результат:* "hello\nworld"
#### Тест М1.8: Создание класса из строки, содержащей комбинацию разных символов (test_combine_constructor)
*Тип теста:* Позитивный

*Описание:* Проверка создания класса из строки, содержащей комбинацию разных символов

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

*Входные данные:* "HeLlO\nмИр!"

*Ожидаемый результат:* "hello\nмир!"
#### Тест М1.9: Создание класса из объекта неподходящего типа(test_unidentified_object)
*Тип теста:* Негативный

*Описание:* Проверка на ошибки при создании класса из объекта неподходящего типа

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

*Входные данные:* []

*Ожидаемый результат:* TypeError("unidentified type object")
#### Тест М1.10: Тестирование декоратора функции шифрования алгоритма Атбаш (передача текста)(test_atbash_cipher_decryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка декоратора функции шифрования алгоритма Атбаш

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.atbash_cipher_decryption(str, alf)}

*Входные данные:* "hello"

*Ожидаемый результат:* "hello"
#### Тест М1.11: Тестирование декоратора функции шифрования алгоритма Атбаш (алфавит по умолчанию)(test_atbash_cipher_decryption_empty_alf)
*Тип теста:* Позитивный

*Описание:* Проверка алфавита по умолчанию в декораторе функции шифрования алгоритма Атбаш

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.atbash_cipher_decryption(str, alf)}

*Входные данные:* Отсутствуют

*Ожидаемый результат:* alf == "abcdefghijklmnopqrstuvwxyz"
#### Тест М1.12: Тестирование декоратора функции шифрования алгоритма Атбаш (передача теста + алфавит по умолчанию)(test_atbash_cipher_decryption_string_and_alf)
*Тип теста:* Позитивный

*Описание:* Проверка передачи текста и алфавита по умолчанию в декораторе функции шифрования алгоритма Атбаш

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.atbash_cipher_decryption(str, alf)}

*Входные данные:* "hello"

*Ожидаемый результат:* "hello", alf = "abcdefghijklmnopqrstuvwxyz"
#### Тест М1.13: Тестирование декоратора функции шифрования алгоритма Атбаш (передача теста и алфавита) (test_atbash_cipher_decryption_alf)
*Тип теста:* Позитивный

*Описание:* Проверка передачи теста и алфавита в декораторе функции шифрования алгоритма Атбаш

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.atbash_cipher_decryption(str, alf)}

*Входные данные:* "hello", alf = "abc"

*Ожидаемый результат:* "hello", alf = "abc"
#### Тест М1.14: Вызов метода шифрования Атбаш из строки из нестрокового объекта (test_atbash_cipher_decryption_raises_type_error_for_invalid_self)
*Тип теста:* Негативный

*Описание:* Проверка вызова метода шифрования строки из нестрокового объекта

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.atbash_cipher_decryption(str, alf)}

*Входные данные:* 123

*Ожидаемый результат:* TypeError("unidentified type object in str")
#### Тест М1.15: Вызов метода шифрования Атбаш из строки с нестроковым алфавитом (test_atbash_unidentified_object_in_alf)
*Тип теста:* Негативный

*Описание:* Проверка вызова метода шифрования строки с нестроковым алфавитом

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.atbash_cipher_decryption(str, alf)}

*Входные данные:* "hello", alf=123

*Ожидаемый результат:* TypeError("unidentified type object in alf")
#### Тест М1.16: Тестирование декоратора функции шифрования алгоритма Цезаря (передача текста)(test_cesar_cipher_decryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка декоратора функции шифрования алгоритма Цезаря

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, step, alf)}

*Входные данные:* "hello"

*Ожидаемый результат:* "hello"
#### Тест М1.17: Тестирование декоратора функции шифрования алгоритма Цезаря(алфавит по умолчанию)(test_cesar_cipher_decryption_empty_alf)
*Тип теста:* Позитивный

*Описание:* Проверка алфавита по умолчанию в декораторе функции шифрования алгоритма Цезаря

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, step, alf)}

*Входные данные:* Отсутствуют

*Ожидаемый результат:* alf == "abcdefghijklmnopqrstuvwxyz"
#### Тест М1.18: Тестирование декоратора функции шифрования алгоритма Цезаря(шаг по умолчанию)(test_cesar_cipher_decryption_empty_step)
*Тип теста:* Позитивный

*Описание:* Проверка шага по умолчанию в декораторе функции шифрования алгоритма Цезаря

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, step, alf)}

*Входные данные:* Отсутствуют

*Ожидаемый результат:* step == 1
#### Тест М1.19: Тестирование декоратора функции шифрования алгоритма Цезаря (передача теста, шаг и алфавит по умолчанию)(test_cesar_cipher_decryption_string_and_alf_and_step)
*Тип теста:* Позитивный

*Описание:* Проверка передачи текста, шаг и алфавита по умолчанию в декораторе функции шифрования алгоритма Цезаря

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, step, alf)}

*Входные данные:* "hello"

*Ожидаемый результат:* "hello", step == 1, alf = "abcdefghijklmnopqrstuvwxyz"
#### Тест М1.20: Тестирование декоратора функции шифрования алгоритма Цезаря(передача теста, шага и алфавита) (test_cesar_cipher_decryption_alf)
*Тип теста:* Позитивный

*Описание:* Проверка передачи теста, шага и алфавита в декораторе функции шифрования алгоритма Цезаря

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, step, alf)}

*Входные данные:* "hello", step = 5, alf = "abc"

*Ожидаемый результат:* "hello", step == 5, alf = "abc"
#### Тест М1.21: Вызов метода шифрования алгоритма Цезаря из строки из нестрокового объекта (test_cesar_cipher_decryption_raises_type_error_for_invalid_self)
*Тип теста:* Негативный

*Описание:* Проверка вызова метода шифрования строки из нестрокового объекта

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, step, alf)}

*Входные данные:* 123

*Ожидаемый результат:* TypeError("unidentified type object in str")
#### Тест М1.23: Вызов метода шифрования алгоритма Цезаря из строки с нечисленным шагом(test_cesar_unidentified_object_in_step)
*Тип теста:* Негативный

*Описание:* Проверка вызова метода шифрования строки с нецелочисленным шагом

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, step, alf)}

*Входные данные:* "hello", step = []

*Ожидаемый результат:* TypeError("unidentified type object in step")
#### Тест М1.23: Вызов метода шифрования алгоритма Цезаря из строки с нецелочисленным шагом(test_cesar_unidentified_object_in_step_float)
*Тип теста:* Негативный

*Описание:* Проверка вызова метода шифрования строки с нецелочисленным шагом

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, step, alf)}

*Входные данные:* "hello", step = 1.5

*Ожидаемый результат:* TypeError("unidentified type object in step")
#### Тест М1.24: Вызов метода шифрования алгоритма Цезаря из строки с нестроковым алфавитом (test_cesar_unidentified_object_in_alf)
*Тип теста:* Негативный

*Описание:* Проверка вызова метода шифрования строки с нестроковым алфавитом

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, step, alf)}

*Входные данные:* "hello", step = 1, alf=123

*Ожидаемый результат:* TypeError("unidentified type object in alf")
#### Тест М1.25: Тестирование метода вызова алгоритма шифрования Вижинера на передачу аргументов(строка, ключ и алфавит)(test_vigenere_cipher_encryption_string_key_alf)
*Тип теста:* Позитивный

*Описание:* Проверка метода вызова алгоритма шифрования Вижинера на передачу аргументов(строка, ключ и алфавит)

*Метод:* CryptographerStr/CryptographerStr.py{vigenere_cipher_encryption(str, key, alf)}

*Входные данные:* (self=CryptographerStr("hello"), key="world", alf="abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* (self == "hello", assert key == "world", assert alf == "abcdefghijklmnopqrstuvwxyz")
#### Тест М1.26: Тестирование метода вызова алгоритма шифрования Вижинера на передачу аргументов(строка и ключ)(test_vigenere_cipher_encryption_string_key_empty_alf)
*Тип теста:* Позитивный

*Описание:* Проверка метода вызова алгоритма шифрования Вижинера на передачу аргументов(строка и ключ)

*Метод:* CryptographerStr/CryptographerStr.py{vigenere_cipher_encryption(str, key, alf)}

*Входные данные:* (self=CryptographerStr("hello"), key="world")

*Ожидаемый результат:* (self == "hello", assert key == "world", assert alf == "abcdefghijklmnopqrstuvwxyz")
#### Тест М1.27: Тестирование метода вызова алгоритма шифрования Вижинера на некорректном объекте(test_vigenere_cipher_encryption_invalid_self)
*Тип теста:* Негативный

*Описание:* Проверка метода вызова алгоритма шифрования Вижинера на некорректном объекте

*Метод:* CryptographerStr/CryptographerStr.py{vigenere_cipher_encryption(str, key, alf)}

*Входные данные:* (self=123, key="world")

*Ожидаемый результат:* TypeError("unidentified type object in str")
#### Тест М1.28: Тестирование метода вызова алгоритма шифрования Вижинера с некорректным ключом(test_vigenere_cipher_encryption_invalide_key)
*Тип теста:* Негативный

*Описание:* Проверка метода вызова алгоритма шифрования Вижинера с некорректным ключом

*Метод:* CryptographerStr/CryptographerStr.py{vigenere_cipher_encryption(str, key, alf)}

*Входные данные:* (self="hello", key=123)

*Ожидаемый результат:* TypeError("unidentified type object in key")
#### Тест М1.29: Тестирование метода вызова алгоритма шифрования Вижинера с некорректным алфавитом(test_vigenere_cipher_encryption_invalide_alf)
*Тип теста:* Негативный

*Описание:* Проверка метода вызова алгоритма шифрования Вижинера с некорректным алфавитом

*Метод:* CryptographerStr/CryptographerStr.py{vigenere_cipher_encryption(str, key, alf)}

*Входные данные:* (self="hello", key="world", alf=123)

*Ожидаемый результат:* TypeError("unidentified type object in alf")
#### Тест М1.30: Тестирование метода вызова алгоритма дешифрования Вижинера на передачу аргументов(строка, ключ и алфавит)(test_vigenere_cipher_decryption_string_key_alf)
*Тип теста:* Позитивный

*Описание:* Проверка метода вызова алгоритма дешифрования Вижинера на передачу аргументов(строка, ключ и алфавит)

*Метод:* CryptographerStr/CryptographerStr.py{vigenere_cipher_decryption(str, key, alf)}

*Входные данные:* (self=CryptographerStr("hello"), key="world", alf="abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* (self == "hello", assert key == "world", assert alf == "abcdefghijklmnopqrstuvwxyz")
#### Тест М1.31: Тестирование метода вызова алгоритма дешифрования Вижинера на передачу аргументов(строка и ключ)(test_vigenere_cipher_decryption_string_key_empty_alf)
*Тип теста:* Позитивный

*Описание:* Проверка метода вызова алгоритма дешифрования Вижинера на передачу аргументов(строка и ключ)

*Метод:* CryptographerStr/CryptographerStr.py{vigenere_cipher_decryption(str, key, alf)}

*Входные данные:* (self=CryptographerStr("hello"), key="world")

*Ожидаемый результат:* (self == "hello", assert key == "world", assert alf == "abcdefghijklmnopqrstuvwxyz")
#### Тест М1.32: Тестирование метода вызова алгоритма дешифрования Вижинера на некорректном объекте(test_vigenere_cipher_decryption_invalid_self)
*Тип теста:* Негативный

*Описание:* Проверка метода вызова алгоритма дешифрования Вижинера на некорректном объекте

*Метод:* CryptographerStr/CryptographerStr.py{vigenere_cipher_decryption(str, key, alf)}

*Входные данные:* (self=123, key="world")

*Ожидаемый результат:* TypeError("unidentified type object in str")
#### Тест М1.33: Тестирование метода вызова алгоритма дешифрования Вижинера с некорректным ключом(test_vigenere_cipher_decryption_invalide_key)
*Тип теста:* Негативный

*Описание:* Проверка метода вызова алгоритма дешифрования Вижинера с некорректным ключом

*Метод:* CryptographerStr/CryptographerStr.py{vigenere_cipher_decryption(str, key, alf)}

*Входные данные:* (self="hello", key=123)

*Ожидаемый результат:* TypeError("unidentified type object in key")
#### Тест М1.34: Тестирование метода вызова алгоритма дешифрования Вижинера с некорректным алфавитом(test_vigenere_cipher_decryption_invalide_alf)
*Тип теста:* Негативный

*Описание:* Проверка метода вызова алгоритма шифрования Вижинера с некорректным алфавитом

*Метод:* CryptographerStr/CryptographerStr.py{vigenere_cipher_decryption(str, key, alf)}

*Входные данные:* (self="hello", key="world", alf=123)

*Ожидаемый результат:* TypeError("unidentified type object in alf")

#### Тест М1.1: 
*Тип теста:* Позитивный

*Описание:* Проверка 

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

*Входные данные:* 

*Ожидаемый результат:* 


# Описание принципов тестирования алгоритмов
Принципы тестирования, применяемые для алгоритмов шифрования, реализованных в данном проекте:
- Шифрование, расшифрование слов и предложений. Шифрование и последующая дешифровка шифрограммы
- Изменение одного символа ключа должно значительно изменять шифрограмму(кроме самых простых алгоритмов шифрования)
- Шифрование и дешифрование пустой строки
- Шифрование и дешифрование строки с одним символом
- Шифрование и дешифрование длинного текста
- Шифрование и дешифрование текста, содержащего символы Unicode (например, "😊", китайские иероглифы)
- Шифрование и дешифрование текста, содержащего числа
- Шифрование и дешифрование текста, содержащего пробелы и символы пунктуации
- Шифрование и дешифрование текста с помощью ключей, состоящих из одинаковых символов, пустого ключа (если допустимо), а также длинных ключей
- Шифрование и дешифрование текста, когда ключ совпадает с текстом
- Шифрование и дешифрование текста, когда ключ состоит только из нулей

# Модульные тесты алгоритмов
### Шифрование Атбаш
#### Тест М2.1: Шифрование строки (test_encryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "Hello", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "Hvool"
#### Тест М2.2: Дешифрование строки (test_decryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования строки

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "Hvool", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "Hello"
#### Тест М2.3: Дешифрование зашифрованной строки (test_encryption_decryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования зашифрованной строки

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "Hello", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "Hello"
#### Тест М2.4: Шифрование пустой строки (test_decryption_empty)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования пустой строки

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* ""
#### Тест М2.5: Шифрование строки из нескольких слов(test_encryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки из нескольких слов

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "Hello world", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "Hvool dliow"
#### Тест М2.6: Дешифрование строки из нескольких слов(test_decryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования строки из нескольких слов

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "Hvool dliow", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "Hello world"
#### Тест М2.7: Шифрование и дешифрование строки (test_encryption_decryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования зашифрованной строки

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "Hello world", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "Hello world"
#### Тест М2.8: Шифрование строки из одного символа 1(test_encryption_one_char_1)
*Тип теста:* Позитивный

*Описание:* Проверка корректности зашифрованной строки из одного символа

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "a", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "z"
#### Тест М2.9: Шифрование строки из одного символа 2(test_encryption_one_char_2)
*Тип теста:* Позитивный

*Описание:* Проверка корректности зашифрованной строки из одного символа

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "c", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "x"
#### Тест М2.10: Шифрование строки из одного символа 3(test_encryption_one_char_3)
*Тип теста:* Позитивный

*Описание:* Проверка корректности зашифрованной строки из одного символа

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "n", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "m"
#### Тест М2.11: Шифрование и дешифрование строки из одного символа (test_encryption_decryption_one_char)
*Тип теста:* Позитивный

*Описание:* Проверка корректности расшифрования зашифрованной строки из одного символа

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "m", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "m"
#### Тест М2.12: Шифрование строки, содержащей символы, отсутствующие в алфавите(test_encryption_missing_characters)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки, содержащей символы, отсутствующие в алфавите

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "Hello, world!", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "Hvool, dliow!"
#### Тест М2.13: Дешифрование строки, содержащей символы, отсутствующие в алфавите(test_decryption_missing_characters)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования строки, содержащей символы, отсутствующие в алфавите

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "Hvool, dliow!", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "Hello, world!"
#### Тест М2.14: Шифрование и дешифрование строки, содержащей символы, отсутствующие в алфавите(test_encryption_decryption_missing_characters)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования зашифрованной строки, содержащей символы, отсутствующие в алфавите

*Метод:* CryptographerStr/atbash_cipher.py{atbash_cipher_decryption(str, alf)}

*Входные данные:* (cipher = "Hello, world!", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "Hello, world!"
### Шифр Цезаря
#### Тест М3.1: Шифрование строки (test_encryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "hello", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "ifmmp"
#### Тест М3.2: Шифрование строки с нулевым шагом(test_zero_step)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки с нулевым шагом

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "hello", step = 0, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "hello"
#### Тест М3.3: Шифрование строки с отрицательным шагом(test_negative_step)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки с отрицательным шагом

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "hello", step = -1, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "gdkkn"
#### Тест М3.4: Шифрование строки с шагом за пределы алфавита(test_big_step)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки с шагом за пределы алфавита

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "xyz", step = 3, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "abc"
#### Тест М3.5: Шифрование строки с отрицательным шагом за пределы алфавита(test_big_step)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки с отрицательным шагом за пределы алфавита

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "abc", step = -3, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "xyz"
#### Тест М3.6: Дешифрование строки (test_decryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования строки

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "ifmmp", step = -1, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "hello"
#### Тест М3.7: Дешифрование пустой строки (test_encryption_decryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования пустой строки

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "hello", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "hello"
#### Тест М3.8: Шифрование пустой строки (test_decryption_empty)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования пустой строки

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* ""
#### Тест М3.9: Шифрование строки из нескольких слов(test_encryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки из нескольких слов

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "hello world", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "ifmmp xpsme"
#### Тест М3.10: Дешифрование строки из нескольких слов(test_decryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования строки из нескольких слов

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "ifmmp xpsme", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "Hello world"
#### Тест М3.11: Шифрование и дешифрование строки (test_encryption_decryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования зашифрованной строки

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "hello world", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "hello world"
#### Тест М3.12: Шифрование строки, содержащей символы, отсутствующие в алфавите(test_encryption_missing_characters)
**Тип теста:** Позитивный

**Описание:** Проверка корректности шифрования строки, содержащей символы, отсутствующие в алфавите

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "Hello, world!", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hfmmp, xpsme!"
#### Тест М3.13: Дешифрование строки, содержащей символы, отсутствующие в алфавите(test_decryption_missing_characters)
**Тип теста:** Позитивный

**Описание:** Проверка корректности дешифрования строки, содержащей символы, отсутствующие в алфавите

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "Hfmmp, xpsme!", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hello, world!"
#### Тест М3.14: Шифрование и дешифрование строки, содержащей символы, отсутствующие в алфавите(test_encryption_decryption_missing_characters)
**Тип теста:** Позитивный

**Описание:** Проверка корректности дешифрования зашифрованной строки, содержащей символы, отсутствующие в алфавите

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "Hello, world!", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hello, world!"
#### Тест М3.15: Шифрование одинаковых строк с одинаковым шагом(test_equal_step)
**Тип теста:** Позитивный

**Описание:** Проверка на то, что при шифровании одинаковых строк с одинаковым шагом возвращаются одинаковые результаты

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "Hello, world!", step_1 = 1, alf = "abcdefghijklmnopqrstuvwxyz")
                    (cipher = "Hello, world!", step_2 = 1, alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** result_1 == result_2
#### Тест М3.16: Шифрование разных строк с одинаковым шагом(test_equal_step_different_string)
**Тип теста:** Негативный

**Описание:** Проверка на то, что при шифровании разных строк с одинаковым шагом возвращаются разные результаты

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher_1 = "Hello, world!", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")
                    (cipher_2 = "Hello!", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** result_1 != result_2
#### Тест М3.17: Шифрование одинаковых строк с разным алфавитом(test_equal_step_different_alf)
**Тип теста:** Негативный

**Описание:** Проверка на то, что при шифровании одинаковых строк с разным алфавитом возвращаются разные результаты

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "Hello, world!", step = 1, alf = "abcdefghijklmnopqrstuvwxyz")
                    (cipher = "Hello, world!", step = 1, alf = "efghijklmnopqrstuvwxyz")

**Ожидаемый результат:** result_1 != result_2
#### Тест М3.18: Шифрование строк с разным шагом(test_diffenert_step)
**Тип теста:** Негативный

**Описание:** Проверка на то, что при шифровании строк с разным шагом возвращаются разные результаты

*Метод:* CryptographerStr/cesar_cipher.py{cesar_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "Hello, world!", step_1 = 1, alf = "abcdefghijklmnopqrstuvwxyz")
                    (cipher = "Hello, world!", step_2 = 2, alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** result_1 != result_2
### Шифр Вижинера
#### Тест М4.1: Шифрование строки (test_encryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}

*Входные данные:* (cipher = "hello", key = "world", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "dscwr"
#### Тест М4.2: Дешифрование строки (test_decryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования строки

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "dscwr", key = "world", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "hello"
#### Тест М4.3: Дешифрование строки с неправильным ключом(test_decryption_invalide_key)
*Тип теста:* Негативный

*Описание:* Проверка на дешифрование с неправильным ключом

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "dscwr", key = "word", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* result != "hello"
#### Тест М4.4: Дешифрование зашифрованной строки(test_decryption_encryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования зашифрованной строки

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)} 
         CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(encryption_string, step, alf)}

*Входные данные:* (cipher = "hello", key = "world", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* "hello"
#### Тест М4.5: Шифрование пустой строки (test_encryption_decryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования зашифрованной строки

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}

*Входные данные:* (cipher = "", key = "world", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* ""
#### Тест М4.6: Дешифрование пустой строки (test_encryption_decryption)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования зашифрованной строки

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "", key = "world", alf = "abcdefghijklmnopqrstuvwxyz")

*Ожидаемый результат:* ""
#### Тест М4.7: Шифрование строки из нескольких слов(test_encryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка корректности шифрования строки из нескольких слов

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}

*Входные данные:* (cipher = "hello world", key = "world", alf = "abcdefghijklmnopqrstuvwxyz ")

*Ожидаемый результат:* "csbwrvjeboz"
#### Тест М4.8: Дешифрование строки из нескольких слов(test_decryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования строки из нескольких слов

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "csbwrvjeboz", key = "world", alf = "abcdefghijklmnopqrstuvwxyz ")

*Ожидаемый результат:* "hello world"
#### Тест М4.9: Шифрование и дешифрование строки (test_encryption_decryption_string)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования зашифрованной строки

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}
         CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "hello world", key = "world", alf = "abcdefghijklmnopqrstuvwxyz ")

*Ожидаемый результат:* "hello world"
#### Тест М4.10: Шифрование строки, состоящей из одного символа(test_encryption_one_symbol)
**Тип теста:** Позитивный

**Описание:** Проверка корректности шифрования строки, состоящей из одного символа

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}

**Входные данные:** (cipher = "a", key = "world", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "w"
#### Тест М4.10: Дешифрование строки, состоящей из одного символа(test_decryption_one_symbol)
**Тип теста:** Позитивный

**Описание:** Проверка корректности дешифрования строки, состоящей из одного символа

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "w", key = "world", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "a"
#### Тест М4.11: Шифрование и дешифрование строки, состоящей из одного символа(test_encryption_decryption_one_symbol)
*Тип теста:* Позитивный

*Описание:* Проверка корректности дешифрования зашифрованной строки

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}
         CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

*Входные данные:* (cipher = "a", key = "world", alf = "abcdefghijklmnopqrstuvwxyz ")

*Ожидаемый результат:* "a"
#### Тест М4.12: Шифрование строки разными ключами(test_encryption_different_keys)
**Тип теста:** Негативный

**Описание:** Проверка совпадения одинаковой строки, зашифрованной разными ключами

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}

**Входные данные:** (cipher = "hello", key_1 = "world", alf = "abcdefghijklmnopqrstuvwxyz")
                    (cipher = "hello", key_2 = "word", alf = "abcdefghijklmnopqrstuvwxyz")
**Ожидаемый результат:** result_1 != result_2
#### Тест М4.12: Шифрование строки разными ключами(test_encryption_different_keys)
**Тип теста:** Негативный

**Описание:** Проверка совпадения одинаковой строки, зашифрованной разными ключами

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}

**Входные данные:** (cipher = "hello", key_1 = "world", alf = "abcdefghijklmnopqrstuvwxyz")
                    (cipher = "hello", key_2 = "word", alf = "abcdefghijklmnopqrstuvwxyz")
**Ожидаемый результат:** result_1 != result_2
#### Тест М4.13: Дешифрование строки разными ключами(test_decryption_different_keys)
**Тип теста:** Негативный

**Описание:** Проверка совпадения одинаковой строки, дешифрованной разными ключами

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "hello", key_1 = "world", alf = "abcdefghijklmnopqrstuvwxyz")
                    (cipher = "hello", key_2 = "word", alf = "abcdefghijklmnopqrstuvwxyz")
**Ожидаемый результат:** result_1 != result_2
#### Тест М4.14: Шифрование строки одинаковыми ключами(test_encryption_string_equal_key)
**Тип теста:** Позитивный

**Описание:** Проверка совпадения одинаковой строки, зашифрованной одинаковыми ключами

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}

**Входные данные:** (cipher = "hello", key_1 = "world", alf = "abcdefghijklmnopqrstuvwxyz")
                    (cipher = "hello", key_2 = "world", alf = "abcdefghijklmnopqrstuvwxyz")
**Ожидаемый результат:** result_1 == result_2
#### Тест М4.15: Дешифрование строки одинаковыми ключами(test_decryption_string_equal_key)
**Тип теста:** Позитивный

**Описание:** Проверка совпадения одинаковой строки, дешифрованной одинаковыми ключами

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "rbhwg", key_1 = "world", alf = "abcdefghijklmnopqrstuvwxyz")
                    (cipher = "rbhwg", key_2 = "world", alf = "abcdefghijklmnopqrstuvwxyz")
**Ожидаемый результат:** result_1 == result_2
#### Тест М4.16: Шифрование строки, содержащей символы, отсутствующие в алфавите(test_encryption_missing_characters)
**Тип теста:** Негативный

**Описание:** Попытка шифрования строки, содержащей символы, отсутствующие в алфавите

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}

**Входные данные:** (cipher = "hello!>", key = "world", alf = "hijklmno")

**Ожидаемый результат:** ValueError("Symbol is missing from the alphabet")
#### Тест М4.17: Шифрование строки с помощью ключа, содержащего символы, отсутствующие в алфавите(test_encryption_missing_characters_in_key)
**Тип теста:** Негативный

**Описание:** Попытка шифрования строки с помощью ключа, содержащего символы, отсутствующие в алфавите

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}

**Входные данные:** (cipher = "hl", key = "world", alf = "hijklmno")

**Ожидаемый результат:** ValueError("Symbol in key is missing from the alphabet")
#### Тест М4.18: Дешифрование строки, содержащей символы, отсутствующие в алфавите(test_decryption_missing_characters)
**Тип теста:** Негативный

**Описание:** Попытка дешифрования строки, содержащей символы, отсутствующие в алфавите

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "hello!>", key = "world", alf = "hijklmno")

**Ожидаемый результат:** ValueError("Symbol is missing from the alphabet")
#### Тест М4.19: Дешифрование строки с помощью ключа, содержащего символы, отсутствующие в алфавите(test_decryption_missing_characters_in_key)
**Тип теста:** Негативный

**Описание:** Попытка дешифрования строки с помощью ключа, содержащего символы, отсутствующие в алфавите

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "hl", key = "world", alf = "hijklmno")

**Ожидаемый результат:** ValueError("Symbol in key is missing from the alphabet")
#### Тест М4.20: Шифрование строки пустой строкой(test_encryption_empty_key)
**Тип теста:** Негативный

**Описание:** Попытка шифрования строки пустой строкой

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_encryption(cipher, step, alf)}

**Входные данные:** (cipher = "hello", key = "", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** ValueError("Empty key")
#### Тест М4.21: Дешифрование строки пустой строкой(test_decryption_empty_key)
**Тип теста:** Негативный

**Описание:** Попытка дешифрования строки пустой строкой

*Метод:* CryptographerStr/vigenere_cipher.py{vigenere_cipher_decryption(cipher, step, alf)}

**Входные данные:** (cipher = "hello", key = "", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** ValueError("Empty key")

# Интеграционные тесты
#### Тест I1.1: Тестирование шифрования алгоритма Атбаш(test_atbash_cipher_decryption)
*Тип теста:* Позитивный

*Описание:* Создание экземпляра CryptographerStr на основе строки и вызов из него метода шифрования алгоритма Атбаш

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.atbash_cipher_decryption(str, alf)}

*Входные данные:* "hello"

*Ожидаемый результат:* "svool"
#### Тест I1.2: Тестирование шифрования и дешифрования алгоритма Атбаш(test_atbash_cipher_encryption_decryption)
*Тип теста:* Позитивный

*Описание:* Создание экземпляра CryptographerStr на основе строки, вызов из него метода шифрования алгоритма Атбаш и вызов метода для дешифровки зашифрованного объекта с тем же ключом

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.atbash_cipher_decryption(str, alf)}

*Входные данные:* "hello"

*Ожидаемый результат:* "hello"
#### Тест I1.3: Тестирование шифрования алгоритма Цезаря(test_cesar_cipher_decryption)
*Тип теста:* Позитивный

*Описание:* Создание экземпляра CryptographerStr на основе строки и вызов из него метода шифрования алгоритма Цезаря

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, alf)}

*Входные данные:* (str="hello", step=1)

*Ожидаемый результат:* "ifmmp"
#### Тест I1.4: Тестирование шифрования и дешифрования алгоритма Цезаря(test_cesar_cipher_encryption_decryption)
*Тип теста:* Позитивный

*Описание:* Создание экземпляра CryptographerStr на основе строки, вызов из него метода шифрования алгоритма Цезаря и вызов метода для дешифровки зашифрованного объекта с обратным ключом

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.cesar_cipher_decryption(str, alf)}

*Входные данные:* (str="hello", step=1)
                  (result_str, step=-1)

*Ожидаемый результат:* "hello"
#### Тест I1.5: Тестирование шифрования алгоритма Вижинера(test_vigenere_cipher_encryption)
*Тип теста:* Позитивный

*Описание:* Создание экземпляра CryptographerStr на основе строки и вызов из него метода шифрования алгоритма Вижинера

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.vigenere_cipher_encryption(str, key)}

*Входные данные:* (str=""hello", key="world)

*Ожидаемый результат:* "dscwr"
#### Тест I1.6: Тестирование ошибок шифрования алгоритма Вижинера(ошибки, обрабатываемые непосредственно алгоритмом)(test_vigenere_cipher_encryption_deep_error)
*Тип теста:* Позитивный

*Описание:* Создание экземпляра CryptographerStr на основе строки и вызов из него метода шифрования алгоритма Вижинера с пустой строкой

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.vigenere_cipher_encryption(str, key)}

*Входные данные:* (str=""hello", key="")

*Ожидаемый результат:* ValueError(match="Empty key")
#### Тест I1.7: Тестирование дешифрования алгоритма Вижинера(test_vigenere_cipher_decryption)
*Тип теста:* Позитивный

*Описание:* Создание экземпляра CryptographerStr на основе строки и вызов из него метода дешифрования алгоритма Вижинера

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.vigenere_cipher_decryption(str, key)}

*Входные данные:* (str=""hello", key="world")

*Ожидаемый результат:* "lqual"
#### Тест I1.6: Тестирование ошибок дешифрования алгоритма Вижинера(ошибки, обрабатываемые непосредственно алгоритмом)(test_vigenere_cipher_decryption_deep_error)
*Тип теста:* Позитивный

*Описание:* Создание экземпляра CryptographerStr на основе строки и вызов из него метода дешифрования алгоритма Вижинера с пустой строкой

*Метод:* CryptographerStr/CryptographerStr.py{CryptographerStr.vigenere_cipher_decryption(str, key)}

*Входные данные:* (str=""hello", key="")

*Ожидаемый результат:* ValueError(match="Empty key")
#### Тест I1.7: Тестирование шифрования и дешифрования алгоритма Вижинера(test_vigenere_cipher_encryption_decryption)
*Тип теста:* Позитивный

*Описание:* Создание экземпляра CryptographerStr на основе строки, вызов из него метода шифрования алгоритма Вижинера и вызов метода дешифрования алгоритма Вижинера из итогового объекта(ключи одинаковы)

*Методы:* CryptographerStr/CryptographerStr.py{CryptographerStr.vigenere_cipher_encryption(str, key)}
          CryptographerStr/CryptographerStr.py{CryptographerStr.vigenere_cipher_decryption(str, key)}

*Входные данные:* (str=""hello", key="world")

*Ожидаемый результат:* "hello"