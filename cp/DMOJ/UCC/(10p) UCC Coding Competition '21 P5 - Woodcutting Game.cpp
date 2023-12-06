#include <bits/stdc++.h>
using namespace std;
int dp [3][301][3][301] = {0}; // Initialize DP array
int f (int h1, int w1, int h2, int w2) {
// If state has already been calculated, return the previously calculated value
if(dp[h1][w1][h2][w2]!=0) return(dp[h1][w1][h2][w2]);
// Recursive base case
 if(h1==1 and w1==1 and h2==1 and w2==1) return dp[1][1][1][1]=-1;
 // If any of the possible moves from OPTION 1 lead to a losing position, this state is a
 // winning position
 for(int i = 1; h1-i > 0; i++)
 if(f(i, w1, h1-i, w1)==-1) return dp[h1][w1][h2][w2] = 1;
 for(int i = 1; w1-i > 0; i++)
 if(f(h1, i, h1, w1-i)==-1) return dp[h1][w1][h2][w2] = 1; 
 for(int i = 1; h2-i > 0; i++)
 if(f(i, w2, h2-i, w2)==-1) return dp[h1][w1][h2][w2] = 1;
 for(int i = 1; w2-i > 0; i++)
 if(f(h2, i, h2, w2-i)==-1) return dp[h1][w1][h2][w2] = 1;
 // If any of the possible moves from OPTION 2 lead to a losing position, this state is a
 // winning position
 if(h1==2)
 if(f(1, w1, h2, w2)==-1) return dp[h1][w1][h2][w2] = 1;
 if(h2==2)
 if(f(h1, w1, 1, w2)==-1) return dp[h1][w1][h2][w2] = 1;
 for(int k = 1; k <= 10 and w1-k >= 1; k++)
 if(f(h1, w1-k, h2, w2)==-1) return dp[h1][w1][h2][w2] = 1;
 for(int k = 1; k <= 10 and w2-k >= 1; k++)
 if(f(h1, w1, h2, w2-k)==-1) return dp[h1][w1][h2][w2] = 1;
 // Otherwise, this state is a losing position.
return dp[h1][w1][h2][w2] = -1;
}
int main() {
 int h1,w1,h2,w2; cin >> h1 >> w1 >> h2 >> w2;
 // Call the recursive function to find the answer.
 if(f(h1,w1,h2,w2)==1)cout << 'W' << endl;
 else cout << 'L'<< endl;
}