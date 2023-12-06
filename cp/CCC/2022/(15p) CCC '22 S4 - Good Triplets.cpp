// https://dmoj.ca/problem/ccc22s4
// 15/15 Clang++

#include <bits/stdc++.h>
#define ll long long
using namespace std;
const ll mx=3e6+9; 
vector<ll>sum,cnt;   
ll n,c; 
ll point(ll a, ll b)
{
     if(a<=b) 
     {
          ll d=sum[b]-(a==0?0:sum[a-1]) ; 
          return d; 
     }
     else 
     {
          ll d=sum[b]+(sum[c-1]-sum[a-1]); 
          return d; 
     }
}
int main()
{
     cin>>n>>c; 
     sum.resize(c); 
     cnt.resize(c);
     for(ll i=0;i<n;i++)
     {
          ll x; cin>>x; 
          cnt[x]++; 
     }
     sum[0]=cnt[0]; 
     for(ll i=1;i<c;i++) sum[i]=sum[i-1]+cnt[i]; 
     ll ans=n*(n-1)*(n-2)/6; 
     for(ll i=0;i<c;i++)
     {
          ll opposite=(i+c/2)%c; 
          ll tot=point(i+1,opposite);
          ans-=cnt[i]*tot*(tot-1)/2; 
          ans-=cnt[i]*(cnt[i]-1)/2*tot; 
          ans-=cnt[i]*(cnt[i]-1)*(cnt[i]-2)/6; 
     }
     if(c%2==0)
     {
          for(ll i=0;i<c/2;i++)
          {
               ll opposite=i+c/2; 
               ans+=cnt[i]*(cnt[i]-1)/2*cnt[opposite]; 
               ans+=cnt[i]*cnt[opposite]*(cnt[opposite]-1)/2; 
          }
     }
     cout<<ans<<endl; 
     
}