# XOR Properties
# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0 

# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
# let's get the flag

from Crypto.Util.number import *
from pwn import xor

KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY2_XOR_KEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'

KEY1 = bytes_to_long(bytes.fromhex(KEY1))
KEY2_XOR_KEY3 = bytes_to_long(bytes.fromhex(KEY2_XOR_KEY3))

KEY1_XOR_KEY2_XOR_KEY3 = KEY2_XOR_KEY3 ^ KEY1

FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2 = bytes_to_long(bytes.fromhex(FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2))
FLAG = FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2 ^ KEY1_XOR_KEY2_XOR_KEY3
FLAG = long_to_bytes(FLAG)
print(FLAG)

# The Flag is: crypto{x0r_i5_ass0c1at1v3}