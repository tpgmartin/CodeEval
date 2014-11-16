# import sys

# test_cases = open(sys.argv[1], 'r')
test_cases = open('data_recovery.txt', 'r')
for test in test_cases:
  text, nums = test.split(';')
  print ' '.join(text.split()[i-1] for i in map(int,nums.split()))
# test_cases.close()

# import sys

# test_cases = open(sys.argv[1], 'r')
# for test in test_cases:
#   if test.strip():
#     string, index = test.split('|')
#     print ''.join(string[i-1] for i in map(int,index.split()))
# test_cases.close()