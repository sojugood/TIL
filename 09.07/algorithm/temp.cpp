#include <iostream>
#include <queue>
#include <tuple>
#include <climits>

using namespace std;

tuple<int, int> direction[] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };

int arr[1000][1000];
int visited[1000][1000][2];

int bfs(int N, int M, int si, int sj, int ei, int ej) {
	queue<tuple<int, int, int, int>> q;

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			visited[i][j][0] = visited[i][j][1] = INT_MAX;
		}
	}

	visited[si][sj][0] = 0;
	q.push({ si, sj, 0, 0 });

	while (!q.empty()) {
		auto[x, y, cnt, wall] = q.front();
		q.pop();

		if (x == ei && y == ej) {
			return cnt;
		}

		for (auto[dx, dy] : direction) {
			int nx = x + dx;
			int ny = y + dy;

			if (0 <= nx && nx < N && 0 <= ny && ny < M) {
				int next_wall = wall + arr[nx][ny];

				if (next_wall <= 1 && visited[nx][ny][next_wall] > cnt + 1) {
					visited[nx][ny][next_wall] = cnt + 1;
					q.push({ nx, ny, cnt + 1, next_wall });
				}
			}
		}
	}

	return -1;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, M;

	cin >> N >> M;

	int Hx, Hy;
	cin >> Hx >> Hy;

	int Ex, Ey;
	cin >> Ex >> Ey;

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			cin >> arr[i][j];
		}
	}

	int result = bfs(N, M, Hx - 1, Hy - 1, Ex - 1, Ey - 1);
	cout << result << endl;

	return 0;
}
