from functions import (
    write_file, 
    caesar_encryption, 
    frequency_analysis, 
    write_json, 
    frequency_decryption)

from paths import (
    encryption_key, 
    decryption_key, 
    encryption_input, 
    decryption_input, 
    encryption_output,
    decryption_output, 
    decryption_frequency)


def main():
    encrypted_text = caesar_encryption(encryption_input, encryption_key)
    write_file(encryption_output, encrypted_text)
    
    frequency = frequency_analysis(decryption_input)
    write_json(decryption_frequency, frequency)
    
    decryption_text = frequency_decryption(decryption_input, decryption_key)
    write_file(decryption_output, decryption_text)


if __name__ == "__main__":
    main()