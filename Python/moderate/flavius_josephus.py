# import sys

# test_cases = open(sys.argv[1], 'r')
test_cases = open('flavius_josephus.txt', 'r')
for test in test_cases:
  l = test.strip().split(",")
  victims = []
  persons, person, increment = range(int(l[0])), int(l[1])-1, int(l[1])
  persons_length = len(persons)
  while len(victims) < persons_length:
    victims.append(persons[person])
    del persons[person]
    person += increment
    person = person % persons_length
  print ' '.join(str(x) for x in victims)
test_cases.close()