# Chinese Remainder theorem is used to solve a system of linear congruences such as:
# x = a1 mod m1, x = a2 mod m2, x = a3 mod m3, ... x = an mod mn
# where m1,m2,m3,...mn are pairwise coprime
# The theorem states that there is a unique solution modulo M = m1*m2*m3*...*mn, x=a1*M1*y1 + a2*M2*y2 + a3*M3*y3 + ... + an*Mn*yn
# where Mi = M/mi and yi is the modular inverse of Mi modulo mi

# example
# x = 2 mod 3, x = 3 mod 11, x = 5 mod 17
M = 3*11*17
M1 = M//3
M2 = M//11
M3 = M//17
y1 = pow(M1,-1,3)
y2 = pow(M2,-1,11)
y3 = pow(M3,-1,17)
a1 = 2
a2 = 3
a3 = 5
x = a1*M1*y1 + a2*M2*y2 + a3*M3*y3
print(x % M)