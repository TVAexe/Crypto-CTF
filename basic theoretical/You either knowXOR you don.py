# I've encrypted the flag with my secret key, you'll never be able to guess it. 
# Please remember the flag format is crypto{.

from pwn import *

# Encrypted data
e = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
e_bytes = bytearray.fromhex(e)

# Flag format: 'crypto{...}'
f = 'crypto{'
f_bytes = f.encode()

# We know the encrypted data were created like this:
# secret_key ^ 'crypto{...}' = e
# We can use the XOR property and change the operands:
# e ^ 'crypto{...}' = secret_key

# XOR the first 7 bytes we know of the flag,
# with the first 7 bytes of the encrypted data
secret_key_7 = xor(f_bytes, e_bytes[0:7])

# key1 = b'myXORke', so we append the 'y' char
secret_key = secret_key_7 + b'y'

# We know the key so decrypt the message and get the flag
flag = xor(secret_key, e_bytes)

print(flag.decode())