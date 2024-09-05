def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
def is_primitive_root(g, p):
    # Calculate p-1
    p_minus_1 = p - 1
    
    # Find all prime factors of p-1
    factors = prime_factors(p_minus_1)
    
    # Check if g^((p-1)/q) mod p != 1 for all factors q
    for factor in factors:
        if pow(g, p_minus_1 // factor, p) == 1:
            return False
    return True

def find_smallest_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g

# Usage
p = 28151
smallest_g = find_smallest_primitive_root(p)
print(smallest_g)
