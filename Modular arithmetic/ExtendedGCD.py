# Let a and b be positive integers.
# The extended Euclidean algorithm is an efficient way to find integers u,v such that
# au+bv=gcd⁡(a,b).

def extended_gcd(a, b):
    if b == 0: # base case
        return (1, 0, a) # u = 1, v = 0, gcd(a, 0) = a
    else:
        x, y, gcd = extended_gcd(b, a % b) # recursive call
        return (y, x - y * (a // b), gcd) # u = y, v = x - y * (a // b), gcd(a, b) = gcd
    
# Example
p=26513
q=32321
print(extended_gcd(p,q)) # (14957, -12204, 1)

