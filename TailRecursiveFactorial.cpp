#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int primer(int num, long long int running_total)
{
    cout << num << endl << running_total << endl;
    if (num == 1)
        return running_total;
    else
        return primer(num-1, running_total*num);
}

int main(){
    int n;
    cin >> n;
    cout << primer(n, 1);
    
    return 0;
}
