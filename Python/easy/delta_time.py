import sys
import math

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  one, two = test.strip().split(' ')
  one = one.split(':')
  two = two.split(':')
  one = int(one[2]) + 60*(int(one[1]) + 60*int(one[0]))
  two = int(two[2]) + 60*(int(two[1]) + 60*int(two[0]))
  difference = one - two
  hours = int(math.floor(difference / 3600))
  minutes = int(math.floor((difference / 60) - hours * 60))
  seconds = int(math.floor(difference - (minutes * 60) - (hours * 60 * 60)))
  if hours < 0:
    hours = -(hours + 1)
    minutes = 59 - minutes
    seconds = 60 - seconds
  print str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
test_cases.close()