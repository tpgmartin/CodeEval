import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = test.strip().split(' ')
  test.sort(key=float)
  print ' '.join(test)
test_cases.close()