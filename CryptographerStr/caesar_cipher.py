def cesar(alf, text, step):
    code_sh = ""
    for char in text:
        for j in range(len(alf)):
            if alf[j] == char:
                c = j
                c += step
                if c >= len(alf):
                    c -= len(alf)
                code_sh += alf[c]
                break  # Прерываем цикл, как только символ найден
    return code_sh

