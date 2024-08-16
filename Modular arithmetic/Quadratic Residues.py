# We say that an integer x is a Quadratic Residue if there exists an a such that a^2 ≡ x mod p 
# If there is no such solution, then the integer is a Quadratic Non-Residue.
p=29
lists =[14,6,11]
#find the quadratic residues of the numbers in the list
for i in lists:
    print(i,[j for j in range(1,p) if j**2 % p == i])
# this is the naive way to find the quadratic residues of a number