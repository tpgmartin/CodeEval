import sys

test_cases = open(sys.argv[1], 'r').read().strip().splitlines()
for test in test_cases:
  x, n = map(int, test.split(','))
  for multiple in xrange(x):
    if multiple * n > x:
      break
  print n * multiple
test_cases.close()