// user.cpp

#include <queue>
#include <tuple>
#include <cstring>

using namespace std;

struct Result {
    int row;
    int col;
};

struct Bacteria {
    int id;
    int size;
    int time;
};

// 배양 시 우선 순위 구조체(dist, row, col 순서)
struct CellPut {
	int dist, row, col;
	bool operator < (CellPut c) const {
		if (dist != c.dist) return dist > c.dist;
		if (row != c.row) return row > c.row;
		return col > c.col;
	}
};

// Id 별 소멸 시간 저장
int BacId[3001];
// 맵
int arr[201][201];
// 현재시간
int curTime;
// N값 전역 사용
int n;
// 상하좌우 이동
pair<int, int> direction[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
// BFS 탐색 시 방문 처리
int visited[201][201];

// Test Case 마다 초기화
void init(int N) {
	memset(arr, 0, sizeof(arr));
	memset(BacId, 0, sizeof(BacId));
	curTime = 0;
	n = N;
}

// 배양 가능 공간 탐색
int bfs(int x, int y) {
	// 여기서는 CellPut 구조체의 dist는 사용되지 않음
	queue<CellPut> q;
	q.push({0, x, y});

	memset(visited, 0, sizeof(visited));
	visited[x][y] = 1;

	int cnt = 0;

	while (!q.empty()) {
		CellPut cur = q.front();
		q.pop();

		cnt++;

		for (auto dir : direction) {
			int dx, dy;
			tie(dx, dy) = dir;
			int nx = cur.row + dx;
			int ny = cur.col + dy;
			if (1 <= nx && nx <= n && 1 <= ny && ny <= n && !visited[nx][ny]) {
				if (BacId[arr[nx][ny]] <= curTime) {
					visited[nx][ny] = 1;
                    q.push({0, nx, ny});
				}
			}
		}
	}
	return cnt;
}

Result putBacteria(int mTime, int mRow, int mCol, Bacteria mBac) {
    Result ret = { 0, 0 };

	curTime = mTime;

	// 해당 좌표에 박테리아가 존재하는지 확인
	if (BacId[arr[mRow][mCol]] > curTime) {
		return ret;
	}

	// 배양 가능 공간 탐색
	int cnt = bfs(mRow, mCol);

	if (cnt < mBac.size) {
		return ret;
	}

	// 배양이 가능하다면 주어진 박테리아 ID의 소멸 시간을 저장한다.
	BacId[mBac.id] = curTime + mBac.time;

	// 이후 우선순위 큐(직접 구현한 구조체)를 사용하여 BFS 탐색
	priority_queue<CellPut> pq;
	pq.push({0, mRow, mCol});
	memset(visited, 0, sizeof(visited));
	visited[mRow][mCol] = 1;

	int put_cnt = 0;

	while (!pq.empty()) {
		CellPut cur = pq.top();
        pq.pop();

		arr[cur.row][cur.col] = mBac.id;

		put_cnt++;

		if (put_cnt == mBac.size) {
			ret.row = cur.row;
			ret.col = cur.col;
			break;
		}

		for (auto dir : direction) {
			int dx, dy;
			tie(dx, dy) = dir;
			int nx = cur.row + dx;
            int ny = cur.col + dy;
            if (1 <= nx && nx <= n && 1 <= ny && ny <= n &&!visited[nx][ny]) {
                if (BacId[arr[nx][ny]] <= curTime) {
                    visited[nx][ny] = 1;
					int dist = abs(mRow - nx) + abs(mCol - ny);
                    pq.push({dist, nx, ny});
                }
            }
		}
	}
    return ret;
}

int killBacteria(int mTime, int mRow, int mCol) {
	curTime = mTime;

	// 현재 시간에 소멸된 박테리아인지 확인한다.
	if (BacId[arr[mRow][mCol]] <= curTime) {
		return 0;
	}

	// 살아있는 박테리아라면 소멸시킨다.
	BacId[arr[mRow][mCol]] = 0;

	// 소멸시킨 박테리아의 ID 리턴
    return arr[mRow][mCol];
}

int checkCell(int mTime, int mRow, int mCol){
	curTime = mTime;

	// 현재 시간에 소멸된 박테리아인지 확인한다.
	if (BacId[arr[mRow][mCol]] <= curTime) {
		return 0;
	}

	// 소멸되지 않은 박테리아면 ID 리턴
    return arr[mRow][mCol];
}