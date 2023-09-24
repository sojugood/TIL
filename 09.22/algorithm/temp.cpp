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
	while (true) {
		int V, E;
		cin >> V >> E;
		
		if (V == 0 && E == 0) {
			return 0;
		}

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

		int total = 0;
		int res = 0;

		for (auto& edge : edges) {
			int c, x, y;
			tie(c, x, y) = edge;
			total += c;
			if (find(parent, x) != find(parent, y)) {
				res += c;
				union_func(parent, x, y);
			}
		}
		cout << total - res << "\n";
	}
}