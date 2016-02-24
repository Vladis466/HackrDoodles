# Given a word ww, rearrange the letters of ww to construct another word ss in such a way that ss is lexicographically greater than ww. In case of multiple possible answers, find the lexicographically smallest one among them.

#Input Format

#The first line of input contains tt, the number of test cases. Each of the next tt lines contains ww.# Enter your code here. Read input from STDIN. Print output to STDOUT


t = int(raw_input())

for var in xrange(t):
    st_str = list(raw_input().lower())
    maxdiff = 0
    pos = 0

    flag = False
    if len(st_str) <= 1:
        print "no answer"
    i = len(st_str)-1

    # find pivot
    while i > 0 and ord(st_str[i - 1]) >= ord(st_str[i]):
          i -= 1
    if i == 0:
        print "no answer"
    else:
        j = i
        piv = i - 1


        # swapping pivot with rightmost successor
        while (j < len(st_str)):
            if ord(st_str[piv]) >= ord(st_str[j]):
                break
            j += 1
        st_str[piv], st_str[j-1] = st_str[j-1], st_str[piv]

        s_nd = len(st_str) - 1
        s_st = piv + 1
        while (s_st < s_nd):
            st_str[s_st], st_str[s_nd] = st_str[s_nd], st_str[s_st]
            s_st += 1
            s_nd -= 1

        nd_str = ''.join(st_str)
        print nd_str
