import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = test.strip()
  print sum(map(lambda n: pow(int(n), len(test)), test)) == int(test)
test_cases.close()