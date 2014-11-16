primes = [2]

for num in range (3,16,2):
  for prime in primes:
    if num % prime != 0:
      primes.append(num)
      break

print primes