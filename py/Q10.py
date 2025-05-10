# 10.Read Print Prime Number in a range using Sieve of  Eratosthenes (Using defind function)


def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


def print_primes_in_range(start, end):
    primes = sieve_of_eratosthenes(end)
    primes_in_range = [p for p in primes if p >= start]
    print(f"Prime numbers between {start} and {end}: {primes_in_range}")


# Example usage
start = 10
end = 50
print_primes_in_range(start, end)
