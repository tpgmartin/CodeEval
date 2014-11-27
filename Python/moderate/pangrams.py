import sys
import string

# test_cases = open(sys.argv[1], 'r')
test_cases = open('pangrams.txt', 'r')
for test in test_cases:
  missing = ''.join([letter for letter in string.ascii_lowercase if letter not in test.strip().lower()])
  print missing if missing else 'NULL'
# test_cases.close()