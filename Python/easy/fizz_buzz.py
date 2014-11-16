import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  output = ''
  F, B, N = test.strip().split(' ')
  F, B, N = int(F), int(B), int(N)
  for x in range(1,N+1):
    if (x % (F * B) == 0):
      output += 'FB '
    elif (x % B == 0):
      output += 'B '
    elif (x % F == 0):
      output += 'F '
    else:
      output += str(x) + ' '
  print output
test_cases.close()