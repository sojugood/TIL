#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>

using namespace std;

int N, M;

tuple<int, int> direction[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

int visited[100][70] = {0};
int visited2[100][70] = {0};
int arr[100][70];

int dfs(int i, int j) {
	for (auto [dx, dy] : direction) {
		int nx, ny;
		nx = i + dx;
		ny = j + dy;
		if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny]) {
			if (arr[nx][ny] > arr[i][j]) {
				return 0;
			}
			else if (arr[nx][ny] == arr[i][j]) {
				visited[i][j] = 1;
				visited2[nx][ny] = 1;
				int tmp;
				tmp = dfs(nx, ny);
				visited[i][j] = 0;
				if (tmp == 0) {
					return 0;
				}
			}
		}
	}
	return 1;
}

int main() {
	cin >> N >> M;

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			int n;
			cin >> n;
			arr[i][j] = n;
		}
	}
	int res = 0;

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (!visited2[i][j]) {
				res += dfs(i, j);
			}
		}
	}
	cout << res << endl;
	return 0;
}