import sys

def n_mod_m(n,m):
  return n if n < m else n_mod_m(n-m,m)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    string = test.strip().split(",")
    n = int(string[0])
    m = int(string[1])
    print n_mod_m(n,m)

test_cases.close()