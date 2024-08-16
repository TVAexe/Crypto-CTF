# Part 1
x = 11 % 6
y = 8146798528947 % 17
print(x,y)

# Part 2
# We'll pick up from the last challenge and imagine we've picked a modulus p, and we will restrict ourselves to the case when p is prime.
# The integers modulo p define a field
# If the modulus is not prime, the set of integers modulo p is not a field, but a ring.
# Lets say we pick p=17. Calculate 3^17 mod 17. It equals to 3
# that is the litte Fermat's theorem.
# Fermat's little theorem states that if p is a prime number, then for any integer a, the number a^p−a is an integer multiple of p or a^(p-1) = 1 mod p
print(pow(273246787654,65536,65537))

# Part 3: Modular Inverse
# As we've seen, we can work within a finite field Fp​, adding and multiplying elements, and always obtain another element of the field.
# For all elements g in the field, there exists a unique integer d such that g⋅d≡1 mod  p
# This is the multiplicative inverse of g.
def modular_inverse(a,b):
    return pow(a,b-2,b)
print(modular_inverse(42,2017))