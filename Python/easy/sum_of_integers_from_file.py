import sys

print sum([int(num.strip()) for num in open(sys.argv[1], 'r').readlines()])