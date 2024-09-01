import requests
from Crypto.Util.number import long_to_bytes, bytes_to_long

# get ciphertext
url = "https://aes.cryptohack.org/symmetry/"
req = requests.get(url + "encrypt_flag/")
ciphertext = bytes.fromhex(req.json()['ciphertext'])
print(ciphertext)
iv = ciphertext[:16]
block = ciphertext[16:]
print(iv, block)
req = requests.get(url + "encrypt/" + block.hex() + "/" + iv.hex() + "/")
print(bytes.fromhex(req.json()['ciphertext']))