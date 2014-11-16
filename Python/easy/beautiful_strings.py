# import sys
import collections
import re

# test_cases = open(sys.argv[1], 'r')
test_cases = open('beautiful_strings.txt', 'r')
for test in test_cases:
  test = re.findall(r'[a-z]', test.strip().lower())
  # test = [ test.strip().lower() ]
  print collections.Counter(test)
# test_cases.close()