#include <iostream>
#include <queue>

using namespace std;

struct Cell {
	int dist, row, col;

	bool operator < (Cell c) const {
		if (dist == c.dist)
			if (row == c.row) return col < c.col;
		return row < c.row;
		return dist < c.dist;
	}
};

Cell a, b;
priority_queue<Cell> pq;

int main() {
	a = { 2, 0, 0 };
	b = { 1, 1, 2 };

	pq.push(a);
	pq.push(b);

	cout << pq.top().dist << "\n";

	return 0;
}