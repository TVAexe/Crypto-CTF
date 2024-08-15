# Given the string label, XOR each character with the integer 13. 
# Convert these integers back to a string and submit the flag as crypto{new_string}.

string = 'label'
key =13
output = ''
for i in string:
    output += chr(ord(i) ^ key)

print('crypto{' + output + '}')

# Output: crypto{aloha}
