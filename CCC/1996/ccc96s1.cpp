#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

typedef long long ll;

const int inf = numeric_limits<int>::max();

int main() {
    fastio;
    int n, a;
    cin >> n;
    while (n--) {
        int c = 0;
        cin >> a;
        for (int x = 1; x < a; x++)
            if (a % x == 0)
                c += x;
            if (c < a)
                printf("%i is a deficient number.\n", a);
            else if (c > a)
                printf("%i is an abundant number.\n", a);
            else
                printf("%i is a perfect number.\n", a);
    }
    return 0;    
}