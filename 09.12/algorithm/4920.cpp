#include <iostream>
#include <algorithm>
#include <cmath>
#include <tuple>
#include <vector>

using namespace std;

int arr[100][100];

int tc = 0;

vector<tuple<int, int>> directions[] = { 
	{ {0, 1}, {0, 2}, {0, 3} },
	{ {1, 0}, {2, 0}, {3, 0} },
	{ {0, 1}, {1, 1}, {1, 2} },
	{ {1, 0}, {1, -1}, {2, -1} },
	{ {0, 1}, {0, 2}, {1, 2} },
	{ {1, 0}, {2, 0}, {2, -1} },
	{ {1, 0}, {1, 1}, {1, 2} },
	{ {0, 1}, {1, 0}, {2, 0} },
	{ {0, 1}, {0, 2}, {1, 1} },
	{ {-1, 1}, {0, 1}, {1, 1} },
	{ {1, -1}, {1, 0}, {1, 1} },
	{ {1, 0}, {1, 1}, {2, 0} },
	{ {0, 1}, {1, 0}, {1, 1} }
};

int main() {
	while (true) {
		ios::sync_with_stdio(0);
		cin.tie(0);
		++tc;
		int N;
		cin >> N;
		if (N == 0) {
			return 0;
		}

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				int n;
				cin >> n;
				arr[i][j] = n;
			}
		}

		int res = -9999999;

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				for (auto direction : directions) {
					int tmp = arr[i][j];
					int tmpcnt = 0;
					for (auto[dx, dy] : direction) {
						int nx, ny;
						nx = i + dx;
						ny = j + dy;
						if (0 <= nx && nx < N && 0 <= ny && ny < N) {
							tmp += arr[nx][ny];
							++tmpcnt;
						}
						else {
							break;
						}
					}
					if (tmpcnt == 3) {
					res = max(res, tmp);
					}
				}
			}
		}
		cout << tc << ". " << res << endl;
	}
}