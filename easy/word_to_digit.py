import sys

nums = {
  'zero' : 0,
  'one'  : 1,
  'two'  : 2,
  'three': 3,
  'four' : 4,
  'five' : 5,
  'six'  : 6,
  'seven': 7,
  'eight': 8,
  'nine' : 9
}

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print ''.join((str(nums.get(i)) for i in test.strip().split(';')))