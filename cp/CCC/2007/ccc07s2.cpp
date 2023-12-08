#include <bits/stdc++.h>

using namespace std;
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3f
#define endl "\n";
using namespace std;
 
using ll = long long;
using db = long double; 
using str = string; 

using pint = pair<int,int>;
using pll = pair<ll,ll>;
using pdb = pair<db,db>;
#define mkpair make_pair
#define f first
#define s second

#define tcT template<class T
#define tcTU tcT, class U

tcT> using V = vector<T>; 
tcT, size_t SZ> using AR = array<T,SZ>; 
using Vint = V<int>;
using Vbool = V<bool>;
using Vll = V<ll>;
using Vdb = V<db>;
using Vstr = V<str>;
using Vpint = V<pint>;
using Vpll = V<pll>;
using Vpdb = V<pdb>;

// vectors
// oops size(x), rbegin(x), rend(x) need C++17
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
tcT> int lwb(V<T>& a, const T& b) { return int(lb(all(a),b)-bg(a)); }
tcT> int upb(V<T>& a, const T& b) { return int(ub(all(a),b)-bg(a)); }

// loops
#define fore(i,a,b) for (int i = (a); i < (b); ++i)
#define for0(i,a) fore(i,0,a)
#define rof(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define rof0(i,a) rof(i,0,a)
#define rep(a) for0(_,a)
#define each(a,x) for (auto& a: x)

const int MOD = (int)1e9+7; // 998244353;
const int MX = (int)2e5+5;
const ll BIG = 1e18; // not too close to LLONG_MAX
const db PI = acos((db)-1);

ll cdiv(ll a, ll b) { return a/b+((a^b)>0&&a%b); } // divide a by b rounded up
ll fdiv(ll a, ll b) { return a/b-((a^b)<0&&a%b); } // divide a by b rounded down

tcT> bool ckmin(T& a, const T& b) {
  return b < a ? a = b, 1 : 0; } // set a = min(a,b)
tcT> bool ckmax(T& a, const T& b) {
  return a < b ? a = b, 1 : 0; } // set a = max(a,b)


int main() {
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  
  int n, m; 
  cin >> n;
  int arr[4][n+1];
  fore(i, 1, n+1) {
    cin >> arr[1][i] >> arr[2][i] >> arr[3][i];
  }
  cin >> m;
  fore(j, 1, m+1) {
  {
    long long smallest = INF;
    int a, b, c; 
    cin >> a >> b >> c;
    for (int i=1; i<=n; i++)
    {
      int aa = arr[1][i], bb = arr[2][i], cc = arr[3][i];
      long long v = aa*bb*cc;
      if ((a<=aa&&b<=bb&&c<=cc)or(a<=aa&&c<=bb&&b<=cc)or(b<=aa&&a<=bb&&c<=cc)or(b<=aa&&c<=bb&&a<=cc)or(c<=aa&&a<=bb&&b<=cc)or(c<=aa&&b<=bb&&a<=cc)) {
        smallest = min(smallest,v);
      }
    }
    if (smallest == INF) {
      cout << "Item does not fit.\n";
    } else {
      cout << smallest << endl;
    } 
  }
}
}