#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

const int mx = 100;

int main() {
    int b, n;
    vector<int> cur(5);
    iota(cur.begin(), cur.end(), 0);
    for (scanf("%i%i", &b, &n); b ^ 4; scanf("%i%i", &b, &n))
    {
        switch(--b)
        {
            case 0:
            case 1:
            {
                if (b)
                    n *= -1;
                vector<int> ne(5);
                for (int x = 0; x < 5; x++)
                    ne[x] = cur[(x+n+5)%5];
                cur = ne;
            }
            break;
            case 2:
                swap(cur[0], cur[1]);
            break;
        }
    }
    for (int x = 0; x < 5; x++)
        printf("%c ", 'A'+cur[x]);
}