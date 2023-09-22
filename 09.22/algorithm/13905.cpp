#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int find(vector<int>& parent, int x) {
	if (parent[x] == x) {
		return x;
	}
	else {
		parent[x] = find(parent, parent[x]);
		return parent[x];
	}
}

void union_func(vector<int>& parent, int a, int b) {
	a = find(parent, a);
	b = find(parent, b);
	if (a < b) {
		parent[b] = a;
	}
	else {
		parent[a] = b;
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, M;
	cin >> N >> M;
	int s, e;
	cin >> s >> e;

	vector<tuple<int, int, int>> edges;

	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		edges.push_back(make_tuple(c, a, b));
	}
	sort(edges.begin(), edges.end());
	reverse(edges.begin(), edges.end());

	vector<int> parent(N + 1);

	for (int i = 0; i <= N; i++) {
		parent[i] = i;
	}

	int res = INT_MAX;

	for (auto& edge : edges) {
		int c, x, y;
		tie(c, x, y) = edge;
		if (find(parent, x) != find(parent, y)) {
			res = min(res, c);
			union_func(parent, x, y);
		}
		if (find(parent, s) == find(parent, e)) {
			cout << res << "\n";
			return 0;
		}
	}
	cout << 0 << "\n";
	return 0;
}