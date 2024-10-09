def add_method(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


@add_method(str)
def caesar_cipher_decryption(self):
    return ' '.join(reversed(self.split()))

