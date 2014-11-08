import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = test.strip()
  words = ','.join(re.findall(r'[a-zA-Z]+', test))
  nums = ','.join(re.findall(r'\d+', test))
  bar = "|" if (words and nums) else ""
  print bar.join((words,nums))
test_cases.close()