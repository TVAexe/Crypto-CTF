# The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a,b).
# There are many tools to calculate the GCD of two integers, but for this task we recommend looking up Euclid's Algorithm.
# We say that for any two integers a,ba,b, if gcd⁡(a,b)=1 then a and b are coprime integers.
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

# Example
a=66528
b=52920 
print(greatest_common_divisor(a,b)) 