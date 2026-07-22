def gcd(a,b):
    rem = b % a
    while rem != 0:
        b = a
        a = rem
        rem = b % a
    return a
print(gcd(25,15))
print(gcd(48,18))

#Another code
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(25,15))
print(gcd(48,18))
