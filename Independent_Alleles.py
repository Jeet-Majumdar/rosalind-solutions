from sympy import binomial

f = open("rosalind_lia.txt")
lines = f.read().split()
f.close()
k = int(lines[0])
N = int(lines[1])

# 1 - (P(0) + P(1) + P(2) + P(3) + ... + P(N))

probabilities = []

p=0.25
q=0.75

def P(n, k):
    # Bernoulli term
    return binomial(2**k, n) * p**n * q**(2**k - n)

independent_terms = [P(n, k) for n in range(N)]
prob_independent = sum(independent_terms)
print(1 - prob_independent)
