import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  distances = sorted(map(int,re.findall(r'\d+', test.strip())))
  trip = []
  trip.append(distances[0])
  [ trip.append(distances[i+1] - distances[i]) for i in xrange(len(distances)-1) ]
  print ','.join(map(str,trip))
test_cases.close()