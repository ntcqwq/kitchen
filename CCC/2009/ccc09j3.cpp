#include <bits/stdc++.h>

using namespace std;

#define INF 0x3f3f3f3f;
#define LINF 0x3f3f3f3f3f3f3f3f;
#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
 
typedef long long ll;
typedef long double db;
typedef string str;

// %d is int
// %f is float
// %s is str
// %c is char

#define scann(x) scanf("%d", &x);
#define scannn(x, y) scanf("%d%d", &x, &y);
#define scans(x) scanf("%s", &x)

#define printn(x) printf("%d\n", x);
#define prints(x) printf("%s\n", x);

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

int r1(int t) {
  if (t < 0)
    t += 2400;
  return t;
}

int r2(int t) {
  if (t >= 2400)
    t -= 2400;
  return t;
}

int r3(int t) {
  if (t % 100 >= 60)
    t += 40;
  return t;
}

#define print(t, n) printf("%d in %s\n", t, n);

int main() {
  cheat;
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int time;
  scann(time);
  print(time, "Ottawa");
  time -= 300;
  time = r1(time);
  print(time, "Victoria");
  time += 100;
  time = r2(time);
  print(time, "Edmonton");
  time += 100;
  time = r2(time);
  print(time, "Winnipeg");
  time += 100;
  time = r2(time);
  print(time, "Toronto");
  time += 100;
  time = r2(time);
  print(time, "Halifax");
  time += 30;
  time = r3(time);
  time = r2(time);
  print(time, "St. John's");

  return 0;
}