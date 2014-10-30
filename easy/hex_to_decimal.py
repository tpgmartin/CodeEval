import sys

hex_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

def hex_to_decimal(hex):
  decimal = 0
  sixteens = 1

  for c in hex:
    decimal += hex_dict[c] * sixteens
    sixteens *= 16

  return decimal

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    string = test.strip()
    string = string[::-1]
    print hex_to_decimal(string)
test_cases.close()