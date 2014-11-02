import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print sum(int(digit) for digit in test.strip())
test_cases.close()