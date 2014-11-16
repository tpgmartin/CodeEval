# import sys

# test_cases = open(sys.argv[1], 'r')
test_cases = open('split_the_number.txt', 'r')
for test in test_cases:
  test = test.strip().split(' ')
  nums, pat = test[0], test[1]
  print pat.spilt('')
# test_cases.close()