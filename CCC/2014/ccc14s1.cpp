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
#define ll long long;
#define endl "\n";

int main() {
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int k;
    cin >> k;
    int listoffriends[k];
    for(int i = 0; i < k; i++){
        listoffriends[i] = i+1;
    }
    
    int m;
    cin >> m;
    
    int r[m];
    for(int i = 0; i < m; i++) {
    cin >> r[i];
    int counter = 0;
        for(int j = 0; j < k; j++) {
            if(listoffriends[j] != 0) {
                counter++;
                if (counter == r[i]) {
                    listoffriends[j] = 0;
                    counter = 0;
                }
            }
            
        }
    }
    for(int i = 0; i < k; i++) {
        if(listoffriends[i] != 0) {
            cout << listoffriends[i] << "\n";
        }
    }

  return 0;
}