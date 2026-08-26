def smallest_prime_factors(n):
# create SPF array
    spf = [0]*(n+1)
#initialize each number with itself
    for i in range (2, n+1):
        spf[i] = i
#find smallest prime factors
    for i in range (2, n+1):
        if spf[i] == i:
           for j in range (i+i, n+1,i):
               if spf[j] == j:
                   spf[j]=i
    return spf
#driver code
n = 10
spf = smallest_prime_factors(n)
print("smallest_prime_factors:")
for i in range (2, n+1):
    print(f"spf = ({i}) = {spf[i]}")

