import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


class SymmetricEncryption:
    def generate_key(self) -> bytes:
        """
        Generate a random symmetric key for ChaCha20.
        Returns:
        - bytes: A randomly generated symmetric key.
        """
        return os.urandom(32)  


    def serialize_nonce(self, nonce: bytes, path: str):
        """
        Serialize the nonce to a file.
        Args:
        - nonce (bytes): Nonce to be serialized.
        - path (str): File path to save the nonce.
        Returns:
        - None.
        """
        with open(path, 'wb') as file:
            file.write(nonce)


    def encrypt_text(self, symmetric_key: bytes, text: bytes) -> bytes:
        """
        Encrypt the text using the provided symmetric key and 16-byte nonce.
        Args:
        - symmetric_key (bytes): Symmetric key for encryption.
        - text (bytes): Text to be encrypted.
        Returns:
        - bytes: Encrypted text, prepended by the 16-byte nonce.
        """
        nonce = os.urandom(16)  
        cipher = Cipher(algorithms.ChaCha20(symmetric_key, nonce[:12]), mode=None) 
        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(text)
        return nonce + encrypted_text  


    def decrypt_text(self, symmetric_key: bytes, encrypted_text: bytes) -> bytes:
        """
        Decrypt the text using the provided symmetric key and 16-byte nonce.
        Args:
        - symmetric_key (bytes): Symmetric key for decryption.
        - encrypted_text (bytes): Encrypted text, prepended by the 16-byte nonce.
        Returns:
        - bytes: Decrypted plaintext.
        """
        nonce = encrypted_text[:16]  
        ciphertext = encrypted_text[16:]
        cipher = Cipher(algorithms.ChaCha20(symmetric_key, nonce[:16]), mode=None) 
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext)
