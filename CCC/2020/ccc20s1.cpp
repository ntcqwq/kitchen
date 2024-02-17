/*<CCC '18 S1 - Voronoi Villages>*/ 
#include <bits/stdc++.h>

using namespace std;

#define INF 0x3f3f3f3f;
#define LINF 0x3f3f3f3f3f3f3f3f;
#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

typedef long long ll;
typedef double db;
typedef string str;

inline void scan(){}
template<typename F, typename... R> inline void scan(F &f,R&... r){cin>>f;scan(r...);}
template <typename F> inline void println(F t){cout<<t<<'\n';}
template<typename F, typename... R> inline void println(F f,R... r){cout<<f<<" ";println(r...);}
inline void print(){}
template<typename F, typename... R> inline void print(F f,R... r){cout<<f;print(r...);}

typedef pair<int, int> pint;
typedef pair<ll, ll> pll;
typedef pair<db, db> pdb;
#define mkp make_pair

#define tcT template<class T
#define tcTU tcT, class U
tcT> using V = vector<T>; 
tcT, size_t SZ> using AR = array<T,SZ>; 

typedef V<int> Vint;
typedef V<Vint> VVint;
typedef V<bool> Vbool;
typedef V<ll> Vll;
typedef V<db> Vdb;
typedef V<str> Vstr;
typedef V<pint> Vpint;
typedef V<pll> Vpll;
typedef V<pdb> Vpdb;
typedef deque<int> Dint;
typedef deque<ll> Dll;

#define size(x) int((x).size())
#define all(x) (x).begin(), (x).end()
#define rll(x) x.rbegin(), x.rend() 
#define sort(x) sort(all(x))  
#define pb push_back
#define eb emplace_back
#define ft front()
#define bk back()

#define lb lower_bound
#define ub upper_bound

#define fore(i, a, b) for (int i = (a); i < (b); ++i)
#define forn(i, a, b) for (int i = (a); i <= (b); ++i)
#define fr(i, a) fore(i, 0, a)
#define rof(i, a, b) for (int i = (b)-1; i >= (a); i--)
#define rf(i, a) rof(i, 0, a)
#define rep(a) for0(_, a)
#define each(a, x) for (auto a: x)

#define rotateL(l, rotationAmount) rotate(l.begin(), l.begin()+rotationAmount, l.end())
#define rotateR(l, rotationAmount) rotate(l.begin(), l.begin()+l.size()-rotationAmount, list.end())

const ll big = 1e18; 
const db pie = acos((db)-1);
const int mod = (int) 1e9+7;

ll ceild(ll a, ll b) { return a / b + ((a ^ b) > 0 && a % b); } // ceil division
ll floord(ll a, ll b) { return a / b - ((a ^ b) < 0 && a % b); } // floor division

tcT> bool ckmin(T& a, const T& b) {
    return b < a ? a = b, 1 : 0; } // set a = min(a,b)
tcT> bool ckmax(T& a, const T& b) {
    return a < b ? a = b, 1 : 0; } // set a = max(a,b)

const int mx = (int) 1e5 + 10;

int N;

int main() {
    cheat;
    scan(N);
    Vpint x(N+1);
    fr (i, N) {
        scan(x[i].first, x[i].second);
    }
    sort(x);
    db ans = -(1e19);
    fore (i, 2, N+1) {
        db p = (db)(x[i].second-x[i-1].second) / (db)(x[i].first-x[i-1].first);
        p = (p < 0 ? -p : p);
        ans = max(ans, p);
    }
    printf("%.1f\n", ans);
}