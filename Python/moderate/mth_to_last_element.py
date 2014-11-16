import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  l = test.strip().split(" ")
  letters, index = l[:-1], int(l[-1])
  try:
      print letters[-index]
  except IndexError:
      pass
test_cases.close()