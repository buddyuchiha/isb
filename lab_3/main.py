from functions.file_working import *
from functions.symmetrical import SymmetricEncryption
from functions.asymmetrical import *


settings = read_json("lab_3/settings.json")
s = read_file(settings["input_text"])
print(s)



key = SymmetricEncryption.generate_key()
private_key2, public_key2 = AsymmetricEncryption.generate_keys()
serealization_public_key(settings["public_key"], public_key2)
serealization_private_key(settings["private_key"], private_key2)
cipher_key = AsymmetricEncryption.encrypt_key(public_key2, key)
write_bytes_file(settings["key"], cipher_key)


print(key)
decrypt_key = AsymmetricEncryption.decrypt_key(private_key2, read_bytes_file(settings["key"]))
print(decrypt_key)
encrypt_text = SymmetricEncryption.encrypt_text(decrypt_key, s)
output = write_bytes_file(settings["output_text"], encrypt_text)
print(output)


decrypt_key = AsymmetricEncryption.decrypt_key(private_key2, read_bytes_file(settings["key"]))
decrypt_text = SymmetricEncryption.decrypt_text(decrypt_key, read_bytes_file(settings["output_text"]))
print(encrypt_text)
print('\n')
write_bytes_file(settings["decrypt_text"], decrypt_text)






