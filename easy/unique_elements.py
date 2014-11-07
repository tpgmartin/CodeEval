import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  nums = map(int, test.strip().split(','))
  print ','.join(map(str, sorted(set(nums))))
test_cases.close()