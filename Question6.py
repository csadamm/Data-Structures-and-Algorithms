import math

def isPrimeFunc(n):
    # 0 and 1 are not a prime number
    if n<2:
        return False
    # 2 is a prime number
    if n == 2:
        return True
    # since 2 is prime, any multiple of 2, i.e any even number is not prime
    if n % 2 == 0:
        return False
    # for each odd number until the sqrt(n)
    # if n has a factor large than sqrt(n), it must also have a matching factor smaller than sqrt(n). therefore, if  no factor exists until sqrt(n), then no factor exists at all
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    # if n is not divisible by all the values in the loop, then n is prime
    return True

def sieve(n):
    isPrime = [True] * (n+1)
    isPrime[0] = False # 0 is Not a prime number
    isPrime[1] = False # 1 is not a prime number

    for i in range(2,int(math.sqrt(n)+1)):
        if isPrime[i]: #If it is still marked true
            for multiple in range(i*i, n+1, i):
                isPrime[multiple] = False #mark composites as false

    return isPrime[n]

'''
So what this code is doing is it creates a list from
0 till the number we inputted, and sets all those numbers
as True. Then we will set 0 and 1 as False since they are not prime
Then we will go through the list until the sqrt(n) and
if a True value is found, we will take take its multiples (starting from its square)
and mark these multiples as False (not prime)

Note: We start from the square of the numbers instead of its first multiple
because it is the more optimised approach. This is because any multiple
of i which is smaller than i^2 will already have been marked from a smaller prime

Example: i = 5:
multiples of 5: 10, 15, 20, 25, 30....
10 would have already been marked when i = 2
15 would have been marked when i = 
20 would have been marked when i = 4
'''
n = int(input("Enter a number: "))
print(f"My Algorithm: {isPrimeFunc(n)}")
print(f"Sieve of Eratosthenes: {sieve(n)}")

'''
Optimisations made:
1. for isPrimeFunc, we instantly declare 1 and multiples of 2 as not prime, and 2 as prime
2. for isPrimeFunc, in the for loop we only look through the odd numbers (since multiples of 2 aren't prime)
3. for both functions, the for loop only goes up until the sqrt(n)
'''
