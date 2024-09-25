import argparse
import json
import logging

from functions.asymmetrical import AsymmetricEncryption
from functions.symmetrical import SymmetricEncryption
from functions.file_working import FileWorking

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """
    Main function for generate keys, encrypt and decrypt.
    """
    parser = argparse.ArgumentParser(description="Manage cryptographic operations")
    parser.add_argument(
        "operation",
        choices=["generate_keys", "encrypt", "decrypt"],
        help="Operation to perform",
    )
    args = parser.parse_args()

    try:
        settings = FileWorking.read_json("lab_3/settings.json")
    except FileNotFoundError:
        logging.error("settings.json not found")
        return
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from settings.json")
        return

    def generate_keys():
        """
        Generate symmetric key by using ChaCha20, asymetric keys and serialize them.
        """
        symmetrical_key = SymmetricEncryption.generate_key()
        private_key, public_key = AsymmetricEncryption.generate_keys()

        FileWorking.serealization_private_key(settings["private_key"], private_key)

        cipher_key = AsymmetricEncryption.encrypt_key(public_key, symmetrical_key)
        FileWorking.write_bytes_file(settings["symmetrical_key"], cipher_key)

        logging.info("Keys generated and saved.")

    def encrypt():
        """
        Encrypt the text by using symmetric key, asymetric keys and serialazie them.
        """
        input_text = FileWorking.read_bytes_file(settings["inputed_text"])

        encrypted_symmetrical_key = FileWorking.read_bytes_file(
            settings["symmetrical_key"]
        )
        private_key = FileWorking.deserealization_private_key(settings["private_key"])
        symmetrical_key = AsymmetricEncryption.decrypt_key(
            private_key, encrypted_symmetrical_key
        )

        encrypted_text = SymmetricEncryption.encrypt_text(symmetrical_key, input_text)
        FileWorking.serialization_nonce(
            settings["symmetrical_nonce"], encrypted_text, encrypted_symmetrical_key
        )
        FileWorking.write_bytes_file(settings["encrypted_text"], encrypted_text)

        logging.info("Text encrypted and saved.")

    def decrypt():
        """
        Decrypth the text by using symmetric and asymetric keys.
        """
        encrypted_text = FileWorking.read_bytes_file(settings["encrypted_text"])
        encrypted_symmetrical_key = FileWorking.read_bytes_file(
            settings["symmetrical_key"]
        )
        private_key = FileWorking.deserealization_private_key(settings["private_key"])

        symmetrical_key = AsymmetricEncryption.decrypt_key(
            private_key, encrypted_symmetrical_key
        )

        decrypted_text = SymmetricEncryption.decrypt_text(
            symmetrical_key, encrypted_text
        )
        FileWorking.write_bytes_file(settings["decrypted_text"], decrypted_text)

        logging.info("Text decrypted and saved.")

    match args.operation:
        case "generate_keys":
            generate_keys()
        case "encrypt":
            encrypt()
        case "decrypt":
            decrypt()
        case _:
            logging.error("Unknown operation.")
            
            
if __name__ == "__main__":
    main()