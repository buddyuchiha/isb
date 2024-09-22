from functions.file import *
from functions.symmetrical import *
from functions.asymmetrical import *


settings = read_json("lab_3/settings.json")
s = read_file(settings["input_text2"])
print(s)
key = SymmetricEncryption.generate_key()
encrypt_text = SymmetricEncryption.encrypt_text(key, s)
output = read_bytes_file(encrypt_text)
print(output)
