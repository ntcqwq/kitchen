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

using namespace std;

int main() {

#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int N, C;
  string d1, d2;
  cin >> N >> d1 >> d2;
  for (int i = 0; i < N; i++) {
    if (d2[i] == 'C') {
      if (d1[i] == 'C') {
        C++;  
      }
    }
  }
  cout << C << endl;
  return 0;
}