/*
Given a list of NN integers, your task is to select KK integers from the list such that its unfairness is minimized.
if (x1,x2,x3,…,xk)(x1,x2,x3,…,xk) are KK numbers selected from the list NN, the unfairness is defined as
max(x1,x2,…,xk)−min(x1,x2,…,xk)
max(x1,x2,…,xk)−min(x1,x2,…,xk)
where max denotes the largest integer among the elements of KK, and min denotes the smallest integer among the elements of KK.
*/


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    int N, K, unfairness = INT_MAX;
    cin >> N >> K;
    int list[N];
    int mindex = 0;
    for (int i=0; i<N; i++)
        cin >> list[i];
    sort(list, list+N);
    
    for (int i=0; i<N-K+1; i++)
    {
        if(list[i+K-1]-list[i] < unfairness)
        {
            mindex = i;
            unfairness = list[i+K-1]-list[i];
        }             
    }
    

    
    
    
    cout << unfairness << "\n";
    return 0;
}
