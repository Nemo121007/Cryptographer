def cesar_cipher_decryption(text, step, alf):
    decrypted_text = ""
    for char in text:
        if char in alf:
            original_idx = alf.index(char)
            new_idx = (original_idx + step) % len(alf)
            decrypted_text += alf[new_idx]
        else:
            decrypted_text += char
    return decrypted_text

