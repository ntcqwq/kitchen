#include <bits/stdc++.h>

using namespace std;
#define ll long long;
#define endl "\n";
#define all(x) x.begin(),x.end()

int main() {
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int x, m;
  cin >> x >> m;
  string n = "No such integer exists.";
  for (int i = 0; i < m; ++i)
  {
    if (x * i % m == 1)
    {
      n = to_string(i);
      break;
    }
  }

  cout << n << endl;
    
  return 0;
}