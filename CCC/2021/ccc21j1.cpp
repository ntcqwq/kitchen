#include<iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
#include <map>
#include <iterator>
#include <set>
#include <queue>
#include <ranges>
#include <numeric>
// #include <bits/stdc++.h>


using namespace std;
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3f
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

  
  int b;
  cin >> b;
  int p = 5 * b - 400;
  cout << p << endl;
  if (p > 100) {
      cout << -1 << endl;
  } else if (p < 100) {
      cout << 1 << endl;
  } else {
      cout << 0 << endl;
}
}