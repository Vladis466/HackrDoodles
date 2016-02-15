#!/usr/bin/py
# Head ends here
def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    #put all values into a dictionary. If it exists,extract
    myDict = {item : 1 for index, item in enumerate(a)}        
    count = 0
    for each in myDict:
        if each + k in myDict:
            count += 1
    print count
    
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    pairs(b,_k)