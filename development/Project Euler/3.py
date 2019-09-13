'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

# 600851475143 sayısının en büyük böleni

import math

def getFactors(num):
    factors = []
    for potentialFactor in range(1, int(math.sqrt(num) + 1)):
        if num % potentialFactor == 0:
            factors.append(potentialFactor)
            factors.append(num // potentialFactor)
    factors.sort()
    return factors

def isPrime(num):
    return len(getFactors(num)) == 2

factors = getFactors(600851475143)
biggestNum = 0
for factor in factors:
    if isPrime(factor) and factor > biggestNum: biggestNum = factor
    
print(biggestNum)


