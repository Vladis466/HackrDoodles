import math
t = int(raw_input().strip())
for each in xrange(t):
    nums = raw_input().split(' ')
    counter = 0
    for each in xrange(int(nums[0]),int(nums[1]) + 1):
        if(math.sqrt(each) - int(math.sqrt(each))  == 0):
            counter += 1
    print counter
