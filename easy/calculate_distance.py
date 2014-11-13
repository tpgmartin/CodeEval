# import sys
import re
import math

# test_cases = open(sys.argv[1], 'r')
test_cases = open('calculate_distance.txt', 'r')
for test in test_cases:
  test = re.findall(r'-?\d+', test)
  x_list = sorted([int(test[i]) for i in range(len(test)) if i % 2 == 0])
  y_list = sorted([int(test[i]) for i in range(len(test)) if i % 2 != 0])
  print int(math.sqrt(math.pow(x_list[1]-x_list[0],2) + math.pow(y_list[1]-y_list[0],2)))