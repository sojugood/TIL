#include <iostream>

using namespace std;

// 부모 노드를 찾는 함수
int getParent(int parent[], int x) {
	if (parent[x] == x) return x;
	return parent[x] = getParent(parent, parent[x]);
}

// 두 부모 노드를 합치는 함수
void unionParent(int parent[], int a, int b) {
	a = getParent(parent, a);
	b = getParent(parent, b);
	if (a < b) parent[b] = a;
	else parent[a] = b;
}

// 같은 부모를 가지는지 확인
int findParent(int parent[], int a, int b) {
	a = getParent(parent, a);
	b = getParent(parent, b);
	if (a == b) return 1;
	return 0;
}

int main() {
	int parent[11];
	for (int i = 1; i <= 10; i++) {
		parent[i] = i;
	}
	unionParent(parent, 1, 2);
	unionParent(parent, 2, 3);
	unionParent(parent, 3, 4);
	unionParent(parent, 5, 6);
	unionParent(parent, 6, 7);
	unionParent(parent, 7, 8);
	cout << "1과 5는 연결되어 있나요?" << " " << findParent(parent, 1, 5) << endl;
	cout << "3의 부모는?" << " " << getParent(parent, 3) << endl;
	unionParent(parent, 2, 6);
	cout << "1과 5는 연결되어 있나요?" << " " << findParent(parent, 1, 5) << endl;
	cout << "5의 부모는?" << " " << getParent(parent, 5) << endl;
	return 0;
}