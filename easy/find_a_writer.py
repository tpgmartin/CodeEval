import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  if test.strip():
    string, index = test.split('|')
    print ''.join(string[i-1] for i in map(int,index.split()))
test_cases.close()