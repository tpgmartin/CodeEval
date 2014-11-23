primes = [2,3]
num = 5
while len(primes) < 1000:
  if all(num % i for i in primes):
    primes.append(num)
  num += 2
print sum(primes)