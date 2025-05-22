from cipher.caesar import ALPHABET
class CaesarCipher:
    
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypted_text(self, plani: str, key: int):
        plaintext = plain.upper()
        encrypted = []
        len_alphabet = len(self.alphabet)
        for i in plaintext:
            letters = self.alphabet.index(i)
            cipher_index = (letter + key) % len_alphabet
            cipher_text = self.alphabet[cipher_index]
            encrypted.append(cipher_index)
        return "".join(encrypted)
    def decrypted_text(self, plani: str, key: int):
        plaintext = plain.upper()
        decrypted = []
        len_alphabet = len(self.alphabet)
        for i in plaintext:
            letters = self.alphabet.index(i)
            cipher_index = (letter - key) % len_alphabet
            cipher_text = self.alphabet[cipher_index]
            decrypted.append(cipher_index)
        return "".join(decrypted)