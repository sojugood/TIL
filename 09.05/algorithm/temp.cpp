#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
using namespace std;

tuple<int, int> direction[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int N, M;

int bfs(int i, int j, vector<vector<char>>& arr) {
    queue<tuple<int, int, int>> q;
    vector<vector<int>> visited(N, vector<int>(M, 0));
    visited[i][j] = 1;
    q.push({i, j, 0});
    int res = INT_MAX;

    while (!q.empty()) {
        int x, y, cnt;
        tie(x, y, cnt) = q.front();
        q.pop();

        if (arr[x][y] == 'W') {
            res = min(res, cnt);
        }

        for (auto [dx, dy] : direction) {
            int nx = x + dx;
            int ny = y + dy;
            if (0 <= nx && N > nx && 0 <= ny && M > ny && !visited[nx][ny]) {
                visited[nx][ny] = 1;
                q.push({nx, ny, cnt + 1});
            }
        }
    }
    return res;
}

int main() {
    int T;
    cin >> T;

    for (int tc = 1; tc <= T; ++tc) {
        cin >> N >> M;

        vector<vector<char>> arr(N, vector<char>(M));

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                cin >> arr[i][j];
            }
        }

        int result = 0;

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (arr[i][j] == 'L') {
                    result += bfs(i, j, arr);
                }
            }
        }
        cout << "#" << tc << " " << result << endl;
    }
    return 0;
}