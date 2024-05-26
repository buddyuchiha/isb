import json
from functions import read_file, write_file, read_json, caesar_encryption, frequency_analysis, write_json
from constants import ALPHABET, FREQUENCY_ANALYSIS
from paths import encryption_key, decryption_key, encryption_input, decryption_input, encryption_output, decryption_output


def main():
    encrypted_text = caesar_encryption(encryption_input, encryption_key)
    write_file(encryption_output, encrypted_text)
    decrypted_key = frequency_analysis(decryption_input)
    write_json(decryption_key, decrypted_key)
if __name__ == "__main__":
    main()