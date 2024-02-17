#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int n, a, b, c, sum = 0;

  cin >> n >> a >> b >> c;

  while (n > 0) {
    if (--n >= 0) {
      a++;
      if (a % 35 == 0) {
        n += 30;
      }
      sum++;
    }
    if (--n >= 0) {
      b++;
      if (b % 100 == 0) {
        n += 60;
      }
      sum++;
    }
    if (--n >= 0) {
      c++;
      if (c % 10 == 0) {
        n += 9;
      }
      sum++;
    }
  }

  cout << "Martha plays " << sum << " times before going broke."
       << "\n";
  return 0;
}