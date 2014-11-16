# import sys

# test_cases = open(sys.argv[1], 'r')
test_cases = open('self_describing_numbers.txt', 'r')
for test in test_cases:
  test = test.strip()
  nums = {}
  output = 0

  for i in range(len(test)):
    print i

  # for n in test:
  #   if n in nums:
  #     nums[n] += 1
  #   else:
  #     nums[n] = 1
  
  # for n in test:
  #   if n == nums[n]:
  #     output += 1
  #   else:
  #     output += 0

  # print 1 if output == len(test) else 0

# test_cases.close()