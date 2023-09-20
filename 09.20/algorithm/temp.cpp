#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <tuple>

using namespace std;

int bfs(int start, vector<vector<int>>& graph) {
    queue<pair<int, int>> q;
    q.push({ start, 0 });
    vector<int> visited(101, 0);
    vector<vector<int>> depth(101);
    visited[start] = 1;

    int dep;
    while (!q.empty()) {
        int node;
        tie(node, dep) = q.front();
        q.pop();

        for (int next : graph[node]) {
            if (!visited[next]) {
                visited[next] = 1;
                depth[dep + 1].push_back(next);
                q.push({ next, dep + 1 });
            }
        }
    }

    return *max_element(depth[dep].begin(), depth[dep].end());
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    //freopen_s(new FILE*, "input.txt", "r", stdin);
    int T = 10;

    for (int tc = 1; tc <= T; ++tc) {
        int l, start;
        cin >> l >> start;

        vector<vector<int>> graph(101);

        for (int i = 0; i < l; i += 2) {
            int u, v;
            cin >> u >> v;
            bool found = false;
            for (int value : graph[u]) {
                if (value == v) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                graph[u].push_back(v);
            }
        }

        cout << "#" << tc << " " << bfs(start, graph) << "\n";
    }

    return 0;
}