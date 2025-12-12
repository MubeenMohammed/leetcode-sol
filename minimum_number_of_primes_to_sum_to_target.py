# Given a positive integer N greater than 1, the task is to find the minimum count of Prime Numbers whose sum is equal to given N.

# Approach 
# For the minimum number of primes whose sum is the given number N, Prime Numbers must be as large as possible. Following are the observation for the above problem statement: 

# Case 1: If the number is prime, then the minimum primes numbers required to make sum N is 1.
# Case 2: If the number is even, then it can be expressed as a sum of two primes as per the Goldbach's Conjecture for every even integer greater than 2. Therefore the minimum prime number required to make the sum N is 2.
# Case 3: If the number is odd: 
# If (N-2) is prime, then the minimum prime number required to make the given sum N is 2.
# Else The minimum prime numbers required to make the given sum N is 3 because:


class Solution:
    # Helper function to check if the number is prime or not
    def checkPrime(self, n):
        for i in range(2, int(n ** (1/2)) + 1):
            if n % i == 0:
                return False
        return True
    def minPrimesToSum(self, n):
        # Case 1: if n is prime
        if self.checkPrime(n):
            return 1
        
        # Case 2: if n is not prime and even
        # Check if the number is an even number and then it can be expressed as sum of 2 primes according Goldbachès Conjecture
        if n % 2 == 0:
            return 2
        
        # Case 3: if the number is odd
            # Case 3.1: if n-2 is prime then minimum primes required is 2
            # Case 3.2: else its 3 since n-3 is even and for even we need 2 and we add 3 to it which makes no of primes to be 3
        if self.checkPrime(n - 2):
            return 2
        else:
            return 3


# Another Variation of the same problem -- limit the no of primes to m

# Problem Description
# You need to find the minimum number of prime numbers that sum up to a given integer n.

# You're given two integers:

# n: the target sum you need to achieve
# m: you can only use the first m prime numbers
# The key rules are:

# You can only select from the first m prime numbers (e.g., if m = 3, you can only use 2, 3, and 5)
# You can use each prime number multiple times (it's a multiset, so repetition is allowed)
# The selected primes must sum to exactly n
# Return the minimum count of primes needed
# If it's impossible to form the sum n using the first m primes, return -1.

# For example:

# If n = 9 and m = 3, you can use primes {2, 3, 5}
# One way: 3 + 3 + 3 = 9 (using three primes)
# Another way: 2 + 2 + 5 = 9 (using three primes)
# The minimum number of primes needed is 3



# Pre-compute first 1000 prime numbers using Sieve of Eratosthenes approach
primes = []
x = 2
M = 1000
while len(primes) < M:
    is_prime = True
    # Check if x is divisible by any prime found so far
    for p in primes:
        # Optimization: only check primes up to sqrt(x)
        if p * p > x:
            break
        if x % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(x)
    x += 1


class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        """
        Find minimum number of primes (from first m primes) that sum to n.
        Uses dynamic programming approach similar to coin change problem.

        Args:
            n: target sum
            m: number of primes to consider (from the pre-computed list)

        Returns:
            Minimum number of primes needed, or -1 if impossible
        """
        # Initialize DP array: f[i] = minimum primes needed to sum to i
        # f[0] = 0 (base case: 0 primes needed for sum 0)
        # f[i] = inf initially for i > 0 (not yet reachable)
        f = [0] + [float('inf')] * n

        # Consider each prime from the first m primes
        for prime in primes[:m]:
            # Update all sums that can be reached by adding this prime
            for i in range(prime, n + 1):
                # f[i] = min(current value, value if we use this prime)
                f[i] = min(f[i], f[i - prime] + 1)

        # Return result: minimum primes for sum n, or -1 if impossible
        return f[n] if f[n] < float('inf') else -1
