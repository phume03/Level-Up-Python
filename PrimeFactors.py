#!/usr/bin/env python
# @author: Phumelela Mdluli
# @assignment: Level Up: Python - Prime Factors
# @date: 16/April/2023
# @description: Recursive function used to produce the prime factorization of a given number, n. These are the prime numbers that when multiplied produce the initial value, n.
# @python version: Python 3
# @notes: has two functions:
#   - non recursive "is_prime" function
#   - recursive "prime_factorization" function

def prime_factorization(n):
    UniquePrimeFactorsOfN = []
    for x in range(1,n+1):
        if n%x==0 and is_prime(x):
            UniquePrimeFactorsOfN.append(x)
    PrimeFactorsOfN = []
    FactorizationRemainder = n
    for y in UniquePrimeFactorsOfN:
        FactorizationRemainder = FactorizationRemainder/y
        PrimeFactorsOfN.append(y)
    if FactorizationRemainder>1:
        MorePrimeFactors = prime_factorization(int(FactorizationRemainder))
        PrimeFactorsOfN = PrimeFactorsOfN + MorePrimeFactors
    PrimeFactorsOfN.sort()
    return PrimeFactorsOfN


def is_prime(n):
    prime = True
    if n==0:
        prime = False
    elif n==1:
        prime = False
    elif n==2:
        prime = True
    else:
        for x in range(2,int(n+1/2)):
            if n%x==0:
                prime = False
                break
            pass
    return prime
