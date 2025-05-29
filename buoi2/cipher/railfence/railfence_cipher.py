class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        """
        Encrypts a plain_text message using the Rail Fence Cipher.

        Args:
            plain_text (str): The message to encrypt.
            num_rails (int): The number of rails to use for the cipher.

        Returns:
            str: The encrypted ciphertext.
        """
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1 # 1 for down, -1 for up

        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        ciphertext = ""
        for rail in rails:
            ciphertext += "".join(rail)
        return ciphertext

    def rail_fence_decrypt(self, cipher_text, num_rails):
        """
        Decrypts a cipher_text message encrypted with the Rail Fence Cipher.

        Args:
            cipher_text (str): The message to decrypt.
            num_rails (int): The number of rails used for encryption.

        Returns:
            str: The decrypted plaintext.
        """
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        # Calculate the length of each rail
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length

        plain_text = ""
        rail_index = 0
        direction = 1

        # Reconstruct the plaintext by traversing the rails
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:] # Remove the character just taken
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        return plain_text
