# Enter your code here. Read input from STDIN. Print output to STDOUT
# N: amount of numbers  K: Amount of times operation is performed  Q: Amount of outputs wanted  

N_K_Q = map(int, raw_input().split(' '))
arr = map(int, raw_input().split(' '))
qries = []       
for ea in xrange(N_K_Q[2]):
    qries.append(input()) 
    
rem = N_K_Q[1]%N_K_Q[0]

for ea in qries:
    if ea < rem:
        temp = rem - ea             #get whats left over         
        print arr[N_K_Q[0]-temp]
    else:
        print arr[ea-rem]