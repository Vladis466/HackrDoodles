#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void maxCombo(int amt)
{   
    if (amt < 3)
    {
        cout << -1;
        return;   
    }
    
    if (amt % 3 == 0)
    {
        for(int i = 0; i < amt; i++)
            cout << "5";
        return;
    }
    else
    {
        
        int fiveCount = (amt / 3) * 3;
        int threeCount = amt % 3;
        int Tswitch = 1;
        
        
        while(Tswitch)
        {
            if(fiveCount % 3 == 0 && threeCount % 5 == 0)
                break;
            if(fiveCount < 0)
            {
                Tswitch = -1;
                break;
            }    
            
            fiveCount -= 1;
            threeCount += 1;
        }   
        if(Tswitch == -1)
        {
            cout << -1;
            return;    
        }
            
        
        for(int i = 0; i < fiveCount; i++)
            cout << 5;
        for(int i = 0; i < threeCount; i++)
            cout << 3;
        
    }
    
    
}
int main(){
    int t;
    int Result;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
        
        maxCombo(n);
        
        cout << endl;
    }
    return 0;
}