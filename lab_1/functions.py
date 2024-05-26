from constants import ALPHABET

import json


def read_file(file_path: str) -> str:
    """
    Read the file.
    Args:
    - file_path (str): The path to the file to be read.
    Returns:
    - str: The content of the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} does not exist") from e
    except Exception as e:
        raise e


def write_file(file_path: str, file_content: str) -> None:
    """
    Write to file.
    Args:
    - file_path (str): The path to the file to be written.
    - content (str): The content to write to the file.
    Returns:
    - None
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_content)
    except Exception as e:
        raise e


def read_json(file_path: str) -> dict:
    """
    Read JSON from file.
    Args:
    - file_path (str): The path to the JSON file to be read.
    Returns:
    - dict: The JSON data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} does not exist") from e
    except Exception as e:
        raise e
    
    
def write_json(file_path: str, file_content: dict) -> None:
    """
    Write a dictionary to a JSON file.
    Args:
    - file_path (str): The path to the file to be written.
    - file_content (dict): The dictionary to write to the file.
    Returns:
    - None
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(file_content, file, indent=4, ensure_ascii=False)
    except Exception as e:
        raise e
    
    
def caesar_encryption(file_text: str, file_key: str) -> str:
    """
    Encrypt text using the Caesar cipher.
    Args:
    - file_text (str): The text to be encrypted.
    - file_key (str): The key value for the Caesar cipher.
    Returns:
    - str: The encrypted text.
    """
    key = read_json(file_key)
    text = read_file(file_text).upper()
    encrypted_result = ''
    
    for char in text:
            if char in ALPHABET:
                encrypted_result += key[char]
            else:
                encrypted_result += char
    return encrypted_result

    
def frequency_analysis(file_text: str) -> dict:
    """
    Perform sorted frequency analysis on the text.
    Args:
    - file_text (str): The text to be analyzed.
    Returns:
    - dict: A dictionary with the sorted frequency.
    """
    frequency = {}
    text = read_file(file_text)
    counter = 0
    
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1    
        counter += 1
    
    for char in frequency:
        frequency[char] /= counter
    
    sorted_frequency = dict(sorted(frequency.items(), key=lambda item: 
        item[1], reverse = True))
    return sorted_frequency
    
    
def frequency_decryption(file_text: str, file_key: str) -> str:
    """
    Decrypt the text
    Args:
    - file_text (str): The text to be decrypted.
    - file_key (key): The key value for the frequency.
    Return: 
    - str: The decrypted text.
    """
    decryption_result = ' '
    text = read_file(file_text)
    key = read_json(file_key)
    
    for char in text:    
        decryption_result += key[char]
    return decryption_result