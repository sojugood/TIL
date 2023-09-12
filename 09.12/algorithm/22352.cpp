#include <iostream>
#include <algorithm>
#include <tuple>
#include <queue>

using namespace std;

int N, M;

int arr[30][30];
int arr3[30][30];

queue<tuple<int, int>> q;

tuple<int, int> direction[] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };

int bfs(int i, int j) {
	int tmp, cnt;
	cnt = 1;
	tmp = arr3[i][j];
	arr3[i][j] = 0;

	q.push({ i, j });

	while (!q.empty()) {
		int x, y;
		tie(x, y) = q.front();
		q.pop();

		for (auto[dx, dy] : direction) {
			int nx, ny;
			nx = x + dx;
			ny = y + dy;
			if (0 <= nx && nx < N && 0 <= ny && ny < M) {
				if (arr3[nx][ny] == tmp) {
					arr3[nx][ny] = 0;
					++cnt;
					q.push({ nx, ny });
				}
			}
		}
	}
	return cnt;
}

int bfs2(int i, int j) {
	int tmp2, cnt2;
	cnt2 = 1;
	tmp2 = arr[i][j];
	arr[i][j] = 0;

	q.push({ i, j, });

	while (!q.empty()) {
		int x, y;
		tie(x, y) = q.front();
		q.pop();

		for (auto[dx, dy] : direction) {
			int nx, ny;
			nx = x + dx;
			ny = y + dy;
			if (0 <= nx && nx < N && 0 <= ny && ny < M) {
				if (arr[nx][ny] == tmp2) {
					arr[nx][ny] = 0;
					++cnt2;
					q.push({ nx, ny });
				}
			}
		}
	}
	return cnt2;
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

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			int n2;
			cin >> n2;
			arr3[i][j] = n2 - arr[i][j];
		}
	}

	int res = 0;
	int res2 = 0;
	int check = 0;

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (arr3[i][j] != 0) {
				if (check == 0) {
					++check;
					res = bfs(i, j);
					res2 = bfs2(i, j);
				}
				else {
					cout << "NO" << endl;
					return 0;
				}
			}
		}
	}
	if (res == res2) {
		cout << "YES" << endl;
	}
	else {
		cout << "NO" << endl;
	}
	return 0;
}