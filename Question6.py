import math

def isPrimeFunc(n):
    # 1 is not a prime number
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

def sieveOfErathoshenes:
    

n = int(input("Enter a number: "))
print(f"My Algorithm: {isPrimeFunc(n)}")
