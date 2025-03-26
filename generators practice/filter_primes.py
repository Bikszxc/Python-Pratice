import sympy

def filter_primes(lst):
    for num in lst:
        if sympy.isprime(num):
            yield num

primes = filter_primes([10, 3, 4, 7, 9, 11])

print(next(primes))  # 3
print(next(primes))  # 7
print(next(primes))  # 11