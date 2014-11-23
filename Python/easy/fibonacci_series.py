import sys

def fibonacci_series(num):
  if num < 1:
    return num
  else:
    return fibonacci_series(num-1) + fibonacci_series(num-2)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print -1 * fibonacci_series(int(test.strip()))
test_cases.close()