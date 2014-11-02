import sys

# test_cases = open(sys.argv[1], 'r')
test_cases = open('swap_case.txt', 'r')
for test in test_cases:
  print ' '.join(letter.swapcase() for letter in test.strip().split())  

# test_cases.close()