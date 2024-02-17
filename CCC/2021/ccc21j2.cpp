#include <bits/stdc++.h>

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
typedef map<char, int> dict;
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

  int n;
  cin >> n;
  int highest = 0;
  string hb = "";
  fore(i, 0, n) {
    string name;
    int bid;
    cin >> name >> bid;
    if (i == 0) {
      hb = name;
      highest = bid;
    } else {
      if (bid > highest) {
        highest = bid;
        hb = name;
      }
    }
  }
  cout << hb << endl;
}