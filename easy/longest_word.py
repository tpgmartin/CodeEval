import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  longest = ''
  longest_length = 0
  words = test.strip().split()
  for word in words:
    word_length = len(word)
    if word_length > longest_length:
      longest = word
      longest_length = word_length 
  print longest
test_cases.close()