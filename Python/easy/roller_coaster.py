import sys
from string import ascii_letters

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = test.strip()
  counter = 1
  output = ''
  for i in range(len(test)):
    if test[i] in ascii_letters:
      if counter > 0:
        output += test[i].upper()
        counter *= -1
      else:
        output += test[i].lower()
        counter *= -1
    else:
      output += test[i]
  print output
test_cases.close()