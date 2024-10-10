# Модульные тесты класса
###### Тест М1: Создание класса из строки(test_create_CryptographerStr)
**Тип теста:** Позитивный

**Описание:** Проверка создания класса из строки

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** "hello"

**Ожидаемый результат:** "hello"
###### Тест М2: Создание класса без аргументов (test_create_CryptographerStr_empty_string)
**Тип теста:** Позитивный

**Описание:** Проверка создания класса без аргументов

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** отсутствуют

**Ожидаемый результат:** ""
###### Тест М3: Перевод строки в нижний регистр (test_lower_case)
**Тип теста:** Позитивный

**Описание:** Проверка перевода строки в нижний регистр при создании класса

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** "HeLlO"

**Ожидаемый результат:** "hello"
###### Тест М4: Обработка нетекстовых символов (test_unusual_symbols)
**Тип теста:** Позитивный

**Описание:** Проверка обработки нетекстовых символов при создании класса

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** "123!@#"

**Ожидаемый результат:** "123!@#"
###### Тест М5: Создание класса из строки, состоящей из нескольких слов (test_string_many_world)
**Тип теста:** Позитивный

**Описание:** Проверка создания класса из строки, содержащей несколько слов (разделитель - пробел)

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** "hello world"

**Ожидаемый результат:** "hello world"
###### Тест М6: Создание класса из неанглоязычной строки (test_non_english_characters)
**Тип теста:** Позитивный

**Описание:** Проверка создания класса из неанглоязычной строки

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** "привет мир"

**Ожидаемый результат:** "привет мир"
###### Тест М7: Создание класса из строки, содержащей символы переноса строки (test_multi_line_string)
**Тип теста:** Позитивный

**Описание:** Проверка создания класса из строки, содержащей символы переноса строки

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** "hello\nworld"

**Ожидаемый результат:** "hello\nworld"
###### Тест М8: Создание класса из строки, содержащей комбинацию разных символов (test_combine_constructor)
**Тип теста:** Позитивный

**Описание:** Проверка создания класса из строки, содержащей комбинацию разных символов

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** "HeLlO\nмИр!"

**Ожидаемый результат:** "hello\nмир!"
###### Тест М1: 
**Тип теста:** Позитивный

**Описание:** Проверка 

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** 

**Ожидаемый результат:** 
###### Тест М1: 
**Тип теста:** Позитивный

**Описание:** Проверка 

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** 

**Ожидаемый результат:** 
###### Тест М1: 
**Тип теста:** Позитивный

**Описание:** Проверка 

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** 

**Ожидаемый результат:** 
###### Тест М1: 
**Тип теста:** Позитивный

**Описание:** Проверка 

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** 

**Ожидаемый результат:** 
###### Тест М1: 
**Тип теста:** Позитивный

**Описание:** Проверка 

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** 

**Ожидаемый результат:** 
###### Тест М1: 
**Тип теста:** Позитивный

**Описание:** Проверка 

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** 

**Ожидаемый результат:** 
###### Тест М1: 
**Тип теста:** Позитивный

**Описание:** Проверка 

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** 

**Ожидаемый результат:** 
###### Тест М1: 
**Тип теста:** Позитивный

**Описание:** Проверка 

**Метод:** CryptographerStr/CryptographerStr.py{CryptographerStr(str)}

**Входные данные:** 

**Ожидаемый результат:** 

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
###### Тест М1: Шифрование строки (test_encryption)
**Тип теста:** Позитивный

**Описание:** Проверка корректности шифрования строки

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "Hello", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hvool"

###### Тест М2: Дешифрование строки (test_decryption)
**Тип теста:** Позитивный

**Описание:** Проверка корректности дешифрования строки

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "Hvool", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hello"

###### Тест М3: Дешифрование зашифрованной строки (test_encryption_decryption)
**Тип теста:** Позитивный

**Описание:** Проверка корректности дешифрования зашифрованной строки

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "Hello", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hello"

###### Тест М4: Шифрование пустой строки (test_decryption_empty)
**Тип теста:** Позитивный

**Описание:** Проверка корректности шифрования пустой строки

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** ""

###### Тест М5: Шифрование строки из нескольких слов(test_encryption_string)
**Тип теста:** Позитивный

**Описание:** Проверка корректности шифрования строки из нескольких слов

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "Hello world", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hvool dliow"

###### Тест М6: Дешифрование строки из нескольких слов(test_decryption_string)
**Тип теста:** Позитивный

**Описание:** Проверка корректности дешифрования строки из нескольких слов

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "Hvool dliow", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hello world"

###### Тест М7: Шифрование и дешифрование строки (test_encryption_decryption_string)
**Тип теста:** Позитивный

**Описание:** Проверка корректности дешифрования зашифрованной строки

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "Hello world", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hello world"

###### Тест М8: Шифрование строки из одного символа 1(test_encryption_one_char_1)
**Тип теста:** Позитивный

**Описание:** Проверка корректности зашифрованной строки из одного символа

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "a", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "z"

###### Тест М9: Шифрование строки из одного символа 2(test_encryption_one_char_2)
**Тип теста:** Позитивный

**Описание:** Проверка корректности зашифрованной строки из одного символа

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "c", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "x"

###### Тест М10: Шифрование строки из одного символа 3(test_encryption_one_char_3)
**Тип теста:** Позитивный

**Описание:** Проверка корректности зашифрованной строки из одного символа

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "n", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "m"

###### Тест М11: Шифрование и дешифрование строки из одного символа (test_encryption_decryption_one_char)
**Тип теста:** Позитивный

**Описание:** Проверка корректности расшифрования зашифрованной строки из одного символа

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "m", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "m"

###### Тест М12: Шифрование строки, содержащей символы, отсутствующие в алфавите(test_encryption_missing_characters)
**Тип теста:** Позитивный

**Описание:** Проверка корректности шифрования строки, содержащей символы, отсутствующие в алфавите

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "Hello, world!", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hvool, dliow!"

###### Тест М13: Дешифрование строки, содержащей символы, отсутствующие в алфавите(test_decryption_missing_characters)
**Тип теста:** Позитивный

**Описание:** Проверка корректности дешифрования строки, содержащей символы, отсутствующие в алфавите

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "Hvool, dliow!", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hello, world!"

###### Тест М14: Шифрование и дешифрование строки, содержащей символы, отсутствующие в алфавите(test_encryption_decryption_missing_characters)
**Тип теста:** Позитивный

**Описание:** Проверка корректности дешифрования зашифрованной строки, содержащей символы, отсутствующие в алфавите

**Метод:** CryptographerStr/atbash_cipher.py{atbash_cipher_decryption}

**Входные данные:** (cipher = "Hello, world!", alf = "abcdefghijklmnopqrstuvwxyz")

**Ожидаемый результат:** "Hello, world!"
