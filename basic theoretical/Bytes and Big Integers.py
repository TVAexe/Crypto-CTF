# Cryptosystems like RSA works on numbers, but messages are made up of characters. 
# How should we convert our messages into numbers so that mathematical operations can be applied?

# The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. 
# This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.
# For example:
# message: HELLO
# ascii bytes of message : [72, 69, 76, 76, 79]
# hex bytes of message: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
# base-16 encode of message: 0x48454c4c4f
# base-10 encode of message: 310400273487 

# Python's PyCryptodome library implements this with the methods bytes_to_long() and long_to_bytes(). 
# You will first have to install PyCryptodome and import it with from Crypto.Util.number import *

n =  11515195063862318899931685488813747395775516287289682636499965282714637259206269 
# convert the number to bytes
import Crypto.Util.number as cun
message = cun.long_to_bytes(n)
print(message)

# the flag is crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}