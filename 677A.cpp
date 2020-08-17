#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,m,cnt=0;
    cin>>n>>m;
    for(int i=0 ; i<n ;i++){
         int x=0;
         cin>>x;
         if(x<=m) cnt++;
         else cnt+=2;
    }
    cout<<cnt<<endl;
    return 0;
}
