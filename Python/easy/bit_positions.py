import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = map(int,(test.strip().split(',')))
  bins = bin(test[0])[2:][::-1]
  print str(bins[test[1]-1] == bins[test[2]-1]).lower()
test_cases.close()