# import sys
import re

# test_cases = open(sys.argv[1], 'r')
test_cases = open('split_the_number.txt', 'r')
for test in test_cases:
  nums, pat = test.strip().split(' ')
  first, second = re.compile(r"[+-]").split(pat)
  op1, op2 = int(nums[:len(first)]), int(nums[len(first):])
  print op1 + op2 if '+' in pat else op1 - op2
# test_cases.close()