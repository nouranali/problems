#include <bits/stdc++.h>

using namespace std;

int main()
{
  long long n,m,stp=0;
   cin>>n>>m;
   int a[m+1];
   a[0]=1;
   for(int i=0 ; i<m ;++i){
    cin>>a[i+1];
   }
   for(int i=0 ;i<m;i++){
    int x= a[i+1]-a[i];
   if(x>0) stp+=x;
   else if(x<0) stp+=x+n;

   }
   cout<<stp;
}
