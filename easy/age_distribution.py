import sys

age_dict = {
  tuple(xrange(3)) : "Still in Mama's arms",
  tuple(xrange(3, 5)) : "Preschool Maniac",
  tuple(xrange(5, 12)) : "Elementary school",
  tuple(xrange(12, 15)) : "Middle school",
  tuple(xrange(15, 19)) : "High school",
  tuple(xrange(19, 23)) : "College",
  tuple(xrange(23, 66)) : "Working for the man",
  tuple(xrange(66, 101)) : "The Golden Years"
}

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = int(test)
  if test in xrange(101):
    for i in age_dict.keys():
        if test in i:
            print age_dict[i]
  else:
    print "This program is for humans"
test_cases.close()