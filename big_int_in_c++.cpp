#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// Programing bigint for finding factorials in C++
void find_factorial(int fctr)
{
    int bigNum[1000] = {0};
    int len = 1;
    int temp = 0;
    bigNum[0] = 1;
    
    int carry = 0;
    for(int i=1; i<=fctr; i++)
    {
        for(int j=0; j<len; j++)            //Go until current length
        {
            temp = bigNum[j]*i + carry;     // multiply current factorial(i) by the current position in the operand and add carry
            bigNum[j] = temp % 10;          // long multiplication done. Now insert the first digt
            carry = temp / 10;              // and carry the rest
        }
        
        while(carry > 0)                    // If the carry is greater than 0, we have to increase the size of the array.
        {                                   // and redistribute the values. We are handling the value in the largest position
            bigNum[len] = carry % 10;       // which is untouched by the previous for loop (the array goes from smallest-largest)
            len++;
            carry /= 10;    
        }
    }
    
    for(int i=len-1; i>=0; i--)
        cout << bigNum[i];
}


int main(){
    int n;
    cin >> n;
    find_factorial(n);

    
    return 0;
}