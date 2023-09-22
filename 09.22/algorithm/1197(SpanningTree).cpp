#include <iostream>
#include <vector>
#include <algorithm>

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
	int V, E;
	cin >> V >> E;

	vector<tuple<int, int, int>> edges;

	for (int i = 0; i < E; i++) {
		int x, y, c;
		cin >> x >> y >> c;
		edges.push_back(make_tuple(c, x, y));
	}
	sort(edges.begin(), edges.end());

	vector<int> parent(V + 1);
	
	for (int i = 0; i <= V; i++) {
		parent[i] = i;
	}

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