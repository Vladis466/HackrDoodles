// Alice recently started learning about cryptography and found that anagrams are very useful. Two strings are anagrams of each other if they have same character set (and frequency of characters) and same length. For example strings "bacdc" and "dcbac" are anagrams, while strings "bacdc" and "dcbad" are not.

// Alice decides on an encryption scheme involving 2 large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. She need your help in finding out this number.

// Given two strings (they can be of same or different length) help her in finding out the minimum number of character deletions required to make two strings anagrams. Any characters can be deleted from any of the strings.


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    string str1;
    string str2;
    
    
    getline(cin, str1);
    getline(cin, str2);
    int len1 = str1.size();
    int len2 = str2.size();
    int i;
    int total;
    map<char, int> myMap;
    for(i = 0; i <26; i++) {
        myMap.insert(pair<char, int>('a'+i, 0));
    }    
    
    map<char, int>::iterator p;
    for(i=0; i<len1; i++)
    {
        p = myMap.find(str1[i]);
        if(p != myMap.end())
            p->second += 1;         
    }
    for(i=0; i<len2; i++)
    {
        p = myMap.find(str2[i]);
        if(p != myMap.end())
            p->second -= 1;         
    }
    
    for(i = 0; i <26; i++) {
        p = myMap.find('a'+i);
        if(p != myMap.end())
            total += abs(p->second);
    }    

    cout << total;
 
    return 0;
}
