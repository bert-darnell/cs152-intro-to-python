def primes_upto(n):
    """ Return a list of all prime numbers less than n using a list comprehension. """

    result = [num for num in range(2,n) if is_prime(num)]
    return result
def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True

print(primes_upto(20))