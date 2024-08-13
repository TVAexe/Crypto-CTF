# ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.
# In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite).
arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag = ''.join([chr(i) for i in arr])
print(flag)

# crypto{ASCII_pr1nt4bl3} is the flag resulting from the above code.