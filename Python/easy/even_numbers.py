import sys

test_cases = open(sys.argv[1], 'r')
test_cases = open('even_numbers.txt', 'r')
for test in test_cases:
    num = int(test.strip())
    print (num + 1) % 2
test_cases.close()