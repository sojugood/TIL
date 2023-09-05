#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
using namespace std;

tuple<int, int> direction[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int N, M;

int bfs(int i, int j, vector<vector<int>>& arr) {
    queue<tuple<int, int>> q;

    int cnt = 1;

    arr[i][j] = 0;
    q.push({i, j});

    while (!q.empty()) {
        int x, y;
        tie(x, y) = q.front();
        q.pop();

        for (auto [dx, dy] : direction) {
            int nx = x + dx;
            int ny = y + dy;
            if (0 <= nx && N > nx && 0 <= ny && M > ny) {
                if (arr[nx][ny] == 1) {
                    cnt += 1;
                    arr[nx][ny] = 0;
                    q.push({nx, ny});
                }
            }
        }
    }
    return cnt;
}

int main() {
    cin >> N >> M;

    vector<vector<int>> arr(N, vector<int>(M));

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> arr[i][j];
        }
    }

    int ans = 0;
    int res = 0;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (arr[i][j] == 1) {
                ++ans;
                res = max(res, bfs(i, j, arr));
            }
        }
    }

    cout << ans << endl;
    cout << res << endl;

    return 0;
}
