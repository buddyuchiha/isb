import json
from cryptography.hazmat.primitives import serialization


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
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} does not exist") from e
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
    

def read_bytes_file(file_path: str) -> bytes:
    """
    Reads the bytes file.
    Args:
    - file_path (str): The path to the file to be read.
    Returns:
    - bytes: The bytes read from the file.
    """
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} does not exist") from e
    except Exception as e:
        raise e


def write_bytes_file(file_path: str, file_content: bytes) -> None:
    """
    Writes the bytes file.
    Args:
    - file_path (str): The path to the file to be written.
    - file_content (bytes): The bytes to write to the file.
    Returns:
    - None
    """
    try:
        with open(file_path, "wb") as file:
            file.write(file_content)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} does not exist") from e
    except Exception as e:
        raise e
        

def serealization_public_key (public_key_path: str, public_key: bytes) -> None:
    public_pem = 'public.pem'
    with open(public_pem, 'wb') as public_out:
        public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
             format=serialization.PublicFormat.SubjectPublicKeyInfo))
        
        
def serealization_private_key (private_key_path: str, private_key: bytes) -> None:
    private_pem = 'private.pem'
    with open(private_pem, 'wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
              format=serialization.PrivateFormat.TraditionalOpenSSL,
              encryption_algorithm=serialization.NoEncryption()))
        
    