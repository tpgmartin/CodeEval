# import sys

# test_cases = open(sys.argv[1], 'r')
test_cases = open('sum_to_zero.txt', 'r')
for test in test_cases:
  nums = test.strip().split(",")
  nums = map(int, nums)
  print nums
  increment = 1
  ways = 0

  while len(nums) / increment >= 4:
    for i in range(len(nums)):
      if sum(nums[i::increment]) == 0:
        ways += 1
      # print nums[i::increment]
    increment += 1
  
  print ways

# test_cases.close()