# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import math
import time

def getPrimeFactors(n):
  if n % 2 == 0: return getPrimeFactors(n // 2) + [2]
  for i in range(3, math.floor(math.sqrt(n)), 2):
    if n % i == 0:
      return getPrimeFactors(n // i) + getPrimeFactors(i)
  return [n]

t = time.process_time()
print(getPrimeFactors(600851475143))
print('solved in {:.10f}'.format(time.process_time() - t, ))
