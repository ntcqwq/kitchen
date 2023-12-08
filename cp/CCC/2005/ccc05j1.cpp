#include <bits/stdc++.h>

using namespace std;
#define endl "\n";
#define all(x) x.begin(),x.end()
#define fore(i,j,n) for(int i=j;i<n;i++)

typedef long long int ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<bool> vb;
typedef pair<string,int> psi;
typedef pair<string,double> psd;
typedef double d;
typedef long double ld;

int main() {
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int d,e,w;
    float a=0, b=0;
    cin >> d >> e >> w;
    if(d>100){
        a=(d-100)*25;
    }
    a+=e*15+w*20;
    a/=100;
    if(d>250){
        b=(d-250)*45;
    }
    b+=e*35+w*25;
    b/=100;
    cout << fixed << setprecision(2) << "Plan A costs " << a << endl;
    cout << fixed << setprecision(2) << "Plan B costs " << b << endl;
    if(a>b){
        cout << "Plan B is cheapest." << endl;
    }
    else if(a<b){
        cout << "Plan A is cheapest." << endl;
    }
    else{
        cout << "Plan A and B are the same price." << endl;
    }
}