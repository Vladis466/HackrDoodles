#Watson gives Sherlock an array AA of length NN. Then he asks him to determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero. 
#Formally, find an ii, such that, AA1+A+A2...A...Ai-1 =A=Ai+1+A+Ai+2...A...AN.

#Input Format 
#The first line contains TT, the number of test cases. For each test case, the first line contains NN, the number of elements in the array AA. The second line for each test case contains NN space-separated integers, denoting the array AA.

#Output Format 
#For each test case print YES if there exists an element in the array, such that the sum of the elements on its left is equal to the sum of the elements on its right; otherwise print NO.



# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for each in xrange(t):
    ndx = int(raw_input())
    

        
    stx = 1
    arr = map(int, raw_input().split(' '))
   
    stsum = arr[0]
    ndsum = sum(arr[2:])    
    
    while(ndsum > stsum):    
            stsum += arr[stx]
            ndsum -= arr[stx+1]
            stx += 1
    if ndx == 1:
        print "YES"   
    elif ndx == 2:
        print "NO"
    elif (ndsum == stsum):
        print "YES"
    else:
        print "NO"