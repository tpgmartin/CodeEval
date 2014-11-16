import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = test.strip()
  length = len(test)
  lower = (sum(1 for l in test if l.lower() == l) * 100.0) / length
  upper = (sum(1 for l in test if l.upper() == l) * 100.0) / length
  print "lowercase: {0:.2f} uppercase: {1:.2f}".format(lower, upper)
test_cases.close()