# For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

# I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

secret = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
secret = bytes.fromhex(secret)

for i in range(256):
    output = ''
    for j in secret:
        output += chr(j ^ i)
    if 'crypto{' in output:
        print(output)
        break

# Output: crypto{0x10_15_my_f4v0ur173_by7e}

