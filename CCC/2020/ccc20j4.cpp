#include <iostream>
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
#include <map>
#include <stdio.h>
#include <bits/stdc++.h>

//https://github.com/bqi343/cp-notebook/blob/master/Implementations/content/contest/CppIO.h

using namespace std;
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3f
#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
 
#define ll long long
#define db long double 
#define str string; 

#define size(x) int((x).size())
#define start(x) begin(x)
#define all(x) start(x), end(x)
#define rAll(x) x.rbegin(), x.rend() 
#define sort(x) sort(all(x)) 
#define resize resize
#define insert insert 
#define pb push_back
#define eb emplace_back
#define ft front()
#define bk back()

#define lb lower_bound
#define ub upper_bound

// tcT> int lwb(V<T>& a, const T& b) { return int(lb(all(a),b)-bg(a)); }
// tcT> int upb(V<T>& a, const T& b) { return int(ub(all(a),b)-bg(a)); }

#define fore(i,a,b) for (int i = (a); i < (b); ++i)
#define for0(i,a) fore(i,0,a)
#define rof(i,a,b) for (int i = (b)-1; i >= (a); i--)
#define rof0(i,a) rof(i,0,a)
#define rep(a) for0(_,a)
#define each(a,x) for (auto& a: x)


const int MOD = (int) 1e9+7; // 998244353
const int MX = (int) 2e5+5;
const ll BIG = 1e18; 
const db PI = acos((db)-1);


int main() {
  cheat;
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  string T,S; cin >> T >> S;
  for (int i = 0; i < S.length(); i++) {
      if (T.find(S) == string::npos) S = S.substr(1) + S.at(0);
      else {
          cout << "yes\n"; 
          return 0;
      }
  }
  cout << "no\n";
  return 0;
}