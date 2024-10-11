def cesar_cipher_decryption(text, step, alf):
    code_sh = ""
    for char in text:
        for j in range(len(alf)):
            if alf[j] == char:
                c = j
                c += step
                if c >= len(alf):
                    c -= len(alf)
                code_sh += alf[c]
                break
    return code_sh

