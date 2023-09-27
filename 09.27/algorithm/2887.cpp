#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

int find(vector<int>& parent, int x) {
	if (parent[x] == x) return x;
	return parent[x] = find(parent, parent[x]);
}

void union_func(vector<int>& parent, int a, int b) {
	a = find(parent, a);
	b = find(parent, b);
	if (a < b) parent[b] = a;
	else parent[a] = b;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N;
	cin >> N;

	vector<pair<int, int>> X, Y, Z;
	vector<tuple<int, int, int>> edges;

	for (int i = 0; i < N; ++i) {
		int x, y, z;
		cin >> x >> y >> z;
		X.push_back({ x, i });
		Y.push_back({ y, i });
		Z.push_back({ z, i });
	}

	sort(X.begin(), X.end());
	sort(Y.begin(), Y.end());
	sort(Z.begin(), Z.end());

	for (int i = 1; i < N; ++i) {
		edges.push_back({ abs(X[i - 1].first - X[i].first), X[i - 1].second, X[i].second });
		edges.push_back({ abs(Y[i - 1].first - Y[i].first), Y[i - 1].second, Y[i].second });
		edges.push_back({ abs(Z[i - 1].first - Z[i].first), Z[i - 1].second, Z[i].second });
	}
	
	sort(edges.begin(), edges.end());

	vector<int> parent(N);
	for (int i = 0; i < N; i++) parent[i] = i;

	int res = 0;
	for (auto& edge : edges) {
		int c, x, y;
		tie(c, x, y) = edge;
		if (find(parent, x) != find(parent, y)) {
			res += c;
			union_func(parent, x, y);
		}
	}

	cout << res << "\n";
	return 0;
	
}
