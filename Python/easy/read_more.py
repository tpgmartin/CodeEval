import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = test.strip()
  if len(test) > 55:
    test = test[:40]
    test = test[0:test.rfind(' ')] if test.rfind(' ') != -1 else test
    print test + '... <Read More>'
  else:
    print test
test_cases.close()