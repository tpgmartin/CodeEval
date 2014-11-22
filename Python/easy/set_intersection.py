import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    a, b = test.strip().split(';')
    list_a, list_b = a.split(','), b.split(',')
    print ','.join(sorted(list(set(list_a).intersection(list_b)), key=lambda x: float(x)))
test_cases.close()