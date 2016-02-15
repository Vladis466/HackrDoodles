# James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

# To do this, he follows two rules:

#  He can reduce the value of a letter, e.g. he can change d to c, but he cannot change c to d.
# In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes a. Once a letter has been changed to a, it can no longer be changed.
# Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.







# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


t = raw_input()

for i in range(0, int(t)):
    Tstr = raw_input()
    
    end = len(Tstr) - 1
    start = 0
    cost = 0
    while(end > start):
        if(Tstr[start] != Tstr[end]):
            cost += abs(ord(Tstr[start])-ord(Tstr[end]))
        end -= 1
        start += 1


    print cost