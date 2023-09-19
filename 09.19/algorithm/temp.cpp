#include <iostream>
using namespace std;

int arr[4][4];
int exist[10000000] = {0};
int result;
int tc;

pair<int, int> direction[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

void dfs(int i, int j, int depth, int order) {
    if (depth == 7) {
        if (exist[order] != tc) {
            exist[order] = tc;
            result++;
        }
        return;
    }
    for (auto [dx, dy] : direction) {
        int nx = i + dx;
        int ny = j + dy;
        if (0 <= nx && nx < 4 && 0 <= ny && ny < 4) {
            dfs(nx, ny, depth + 1, order + (pow(10, depth) * arr[i][j]));
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin >> T;

    for (tc = 1; tc <= T; ++tc) {
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> arr[i][j];
            }
        }

        result = 0;

        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                dfs(i, j, 0, 0);
            }
        }

        cout << "#" << tc << " " << result << "\n";
    }

    return 0;
}