import math

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def zeta(s, n):
    return 1 / n**s

def dirichlet_eta(s, n):
    return (-1)**(n+1) / n**s

def modified_eta_odd(s, n):
    return (-1)**(n+1) / (2*n-1)**s

def bernoulli(n):
    if n == 0:
        return 1
    elif n == 1:
        return -1/2
    elif n % 2 == 1 and n > 1:
        return 0
    else:
        a = [0] * (n + 1)
        for m in range(n + 1):
            a[m] = 1 / factorial(m) * sum((-1)**k * math.comb(m, k) * (m - k)**n for k in range(m + 1))
        return a[0] / (n + 1)

from fractions import Fraction as Fr
def bernoulli(n):
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = Fr(1, m+1)
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
    return A[0] # (which is Bn)

def compute_zeta(s):
    assert s > 1, "s must be greater than 1"
    assert s % 2 == 0, "s must be even"
    return 2**(s-1) * (-1)**(s/2+1) * bernoulli(s) / (factorial(s)) * math.pi**s

def compute_dirichlet_eta(s):
    assert s > 1, "s must be greater than 1"
    assert s % 2 == 0, "s must be even"
    return (1-2**(1-s)) * compute_zeta(s)

if __name__ == "__main__":
    # Example usage
    s = 2
    n = 100
    print(f"Zeta({s}, {n}) = {zeta(s, n)}")
    print(f"Dirichlet Eta({s}, {n}) = {dirichlet_eta(s, n)}")
    print(f"Modified Eta Odd({s}, {n}) = {modified_eta_odd(s, n)}")
    print(f"Bernoulli({s}) = {bernoulli(s)}")
    print(f"Compute Zeta({s}) = {compute_zeta(s)}")
    print(f"Compute Dirichlet Eta({s}) = {compute_dirichlet_eta(s)}")