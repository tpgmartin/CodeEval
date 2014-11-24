import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  chars, remove = test.strip().split(',')
  print chars.translate(None, remove.lstrip())
test_cases.close()