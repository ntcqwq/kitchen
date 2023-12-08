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

  int x, y, z;
  cin >> x >> y >> z;
  int bozo[3] = {x, y, z};
  sort(bozo, bozo + 3);
  cout << bozo[1] << endl;
}