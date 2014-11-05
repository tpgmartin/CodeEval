import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = test.split(':')[0].strip().split(' ')
    pos = test.split(':')[1].strip().split(',')
    for i in pos:
      index = i.split('-')
      nums[int(index[1])], nums[int(index[0])] = nums[int(index[0])], nums[int(index[1])]
    print ' '.join(nums)
test_cases.close()