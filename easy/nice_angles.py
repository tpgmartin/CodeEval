import sys

def leading_zero(num):
  if num < 10:
    num = '0' + str(num)
  return num

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = float(test.strip())
  degs = str(int(test))
  mins = leading_zero(int((test - int(degs)) * 60))
  secs = leading_zero(int(((test - int(degs)) * 60 - int(mins)) * 60))
  print "%s.%s\'%s\"" % (degs, mins,secs)
test_cases.close()