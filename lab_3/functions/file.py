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