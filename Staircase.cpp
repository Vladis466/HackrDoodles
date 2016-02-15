#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    int y;
    cin >> n;

    for(int i = n; i > 0; i--)
    {
        y=0;
        while (y < n)
        {
            if (y < i -1)
                cout << " ";
            else
                cout << "#";
            y++;
        }
        
        cout << endl;
    }
    return 0;
    
}
