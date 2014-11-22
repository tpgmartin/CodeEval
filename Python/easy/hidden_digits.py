import sys
import re

letters = {
  'a'    : 0,
  'b'    : 1,
  'c'    : 2,
  'd'    : 3,
  'e'    : 4,
  'f'    : 5,
  'g'    : 6,
  'h'    : 7,
  'i'    : 8,
  'j'    : 9,
}

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  string = test.strip()
  chars, nums = re.findall(r'[a-j]', string), re.findall(r'[0-9]', string)
  chars = [str(letters[chars[i]]) for i in xrange(len(chars))]
  print ''.join(chars + nums) if len(chars + nums) != 0 else 'NONE'
test_cases.close()