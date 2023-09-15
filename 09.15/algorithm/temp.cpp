#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <tuple>

using namespace std;

map<int, vector<tuple<int, int, int>>> direction = {
	{0, {{-1, 0, 1}, {0, -1, 0}, {1, 0, 3}, {0, 1, 2}}},
	{1, {{0, 1, 2}, {-1, 0, 1}, {0, -1, 0}, {1, 0, 3}}},
	{2, {{1, 0, 3}, {0, 1, 2}, {-1, 0, 1}, {0, -1, 0}}},
	{3, {{0, -1, 0}, {1, 0, 3}, {0, 1, 2}, {-1, 0, 1}}}
};

int T, N, M;

int dfs(int i, int j, int rot, int day, int cnt, queue<tuple<int, int, int>>&lst, vector<vector<int>>& arrs, vector<vector<int>>& visited) {
	if (day == 0) {
		return cnt;
	}

	size_t lstSize = lst.size();
	for (size_t _ = 0; _ < lstSize; ++_) {
		int x, y, w;
		tie(x, y, w) = lst.front();
		lst.pop();
		--w;

		if (w == 0) {
			arrs[x][y] = 2;
		}
		else if (w == 1) {
			arrs[x][y] = 3;
			lst.push({ x, y, w });
		}
		else {
			lst.push({ x, y, w });
		}
	}

	bool check = false;

	if (arrs[i][j] == 0) {
		for (auto[dx, dy, r] : direction[rot]) {
			int ni, nj;
			ni = i + dx;
			nj = j + dy;
			if (0 <= ni && ni < N && 0 <= nj && nj < N) {
				if (arrs[ni][nj] != 1) {
					arrs[i][j] = 1;
					lst.push({ i, j, 5 + visited[i][j] });
					visited[i][j] += 1;
					check = true;
					return dfs(ni, nj, r, day - 1, cnt, lst, arrs, visited);
				}
			}
		}
		if (check == false) {
			return dfs(i, j, rot, day - 1, cnt, lst, arrs, visited);
		}
	}
	else if (arrs[i][j] == 2) {
		for (auto[dx, dy, r] : direction[rot]) {
			int ni, nj;
			ni = i + dx;
			nj = j + dy;
			if (0 <= ni && ni < N && 0 <= nj && nj < N) {
				if (arrs[ni][nj] != 1) {
					arrs[i][j] = 0;
					check = true;
					return dfs(ni, nj, r, day - 1, cnt + 1, lst, arrs, visited);
				}
			}
		}
		if (check == false) {
			arrs[i][j] = 0;
			return dfs(i, j, rot, day - 1, cnt + 1, lst, arrs, visited);
		}
	}
}


int main() {
	//freopen_s(new FILE*, "input.txt", "r", stdin);
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		cin >> N >> M;
		vector<vector<int>> arr(N, vector<int>(N));

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				int n;
				cin >> n;
				arr[i][j] = n;
			}
		}

		int result = 0;

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (arr[i][j] == 0) {
					for (int k = 0; k < 4; ++k) {
						vector<vector<int>> arrs = arr;
						vector<vector<int>> visited(N, vector<int>(N, 1));
						queue<tuple<int, int, int>> lst;
						result = max(result, dfs(i, j, k, M, 0, lst, arrs, visited));
					}
				}
			}
		}
		cout << "#" << tc << " " << result << endl;
	}
	return 0;
}