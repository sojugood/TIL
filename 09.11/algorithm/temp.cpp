#include <iostream>
#include <algorithm>
#include <queue>
#include <tuple>

tuple<int, int> direction[] = { {1, 0}, { -1, 0 }, { 0, 1 }, { 0, -1 } };
int arr[50][50];

using namespace std;

int main() {
	int R, C, T;
	cin >> R >> C >> T;

	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			int Arc;
			cin >> Arc;
			arr[i][j] = Arc;
			if (Arc == -1) {

			}
		}
	}

	
}