def primes_up_to(n: int) -> list[int]:
    """
    Difference from the C++ version:
    In C++, extracting the final list of primes typically requires a traditional 
    for-loop iterating over a `std::vector<bool>` or an array. In Python, 
    we can use a list comprehension (`[p for p, prime in enumerate(is_prime) if prime]`) 
    to filter and return the results in a single, concise, and Pythonic line.
    """
    if n < 2:
        return []
        
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
                
    return [p for p, prime in enumerate(is_prime) if prime]