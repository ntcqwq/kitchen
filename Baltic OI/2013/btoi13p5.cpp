#include <bits/stdc++.h>

using namespace std;

#define endl "\n"
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr)

typedef long long ll;
typedef pair<int, int> pint;
typedef vector<int> vint;

const float inf = numeric_limits<float>::infinity();

int H, W;
vector<vector<int>> grid;
vector<vector<bool>> vis;
deque<pair<int, int>> q2;
int ans, t;

vector<pair<int, int>> d = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

void bfs(int t) {
    deque<pair<int, int>> q = q2;
    q2.clear();
    
    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop_front();
        
        for (const auto& dir : d) {
            int na = dir.first;
            int nb = dir.second;
            int ny = y + na;
            int nx = x + nb;
            
            if (ny >= 0 && ny < H && nx >= 0 && nx < W) {
                if (!vis[ny][nx] && grid[ny][nx] != -1) {
                    if (grid[ny][nx] == t) {
                        q.push_back({ny, nx});
                        vis[ny][nx] = true;
                    } else {
                        if (q2.empty()) {
                            ans++;
                        }
                        q2.push_back({ny, nx});
                        vis[ny][nx] = true;
                    }
                }
            }
        }
    }
}

int main() {
	fastio;
    cin >> H >> W;
    grid.assign(H, vector<int>(W));
    vis.assign(H, vector<bool>(W, false));

    for (int i = 0; i < H; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < W; j++) {
            char e = row[j];
            if (e == '.') {
                grid[i][j] = -1;
            } else if (e == 'F') {
                grid[i][j] = 1;
            } else if (e == 'R') {
                grid[i][j] = 0;
            }
        }
    }

    d = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    q2.push_back({0, 0});
    ans = 1;
    t = grid[0][0];

    int i = 1;
    while (true) {
        bfs(t);
        i++;
        if (ans != i) {
            break;
        }
        t ^= 1;
    }

    cout << ans << endl;

    return 0;
}