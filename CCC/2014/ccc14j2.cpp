#include<iostream>

using namespace std;

int main() {

#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int v;
  cin >> v;
  string s;
  cin >> s;
  int acount = 0;
  int bcount = 0;
  for (int i = 0; i < s.size(); i++)
    if (s[i] == 'A') {
      acount += 1;
    } else if (s[i] == 'B') {
      bcount += 1;
    }
  if (acount > bcount) {
    cout << 'A' << endl;
  } else if (acount < bcount) {
    cout << 'B' << endl;
  } else {
    cout << "Tie" << endl;
  }
  
  return 0;
}