# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
t = int(raw_input().strip())
for each in xrange(t):
    nums = raw_input().split(' ')
    counter = 0
    for each in xrange(int(math.ceil(math.sqrt(float(nums[0])))),int(math.ceil(math.sqrt(float(nums[1]) + 1)))):
        counter += 1
    print counter