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