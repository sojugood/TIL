#include <vector>
#include <queue>
#include <algorithm>

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

struct CellInfo {
    int id;
    int endTime;
};

struct Cell {
    int dist, row, col;

    bool operator < (const Cell& c) const {
        if (dist != c.dist) return dist > c.dist; 
        if (row != c.row) return row > c.row;
        return col > c.col;                     
    }
};

vector<vector<CellInfo>> grid;
int N, curTime;
int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

void init(int n) {
    N = n;
    grid = vector<vector<CellInfo>>(N, vector<CellInfo>(N, {0, 0}));
}

void removeExpiredBacteria(int mTime) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (grid[i][j].endTime <= mTime) {
                grid[i][j] = {0, 0};
            }
        }
    }
}

int bfs(int y, int x) {
    queue<pair<int, int>> q;
    q.push({y, x});

    int availableCells = 1;
    vector<vector<bool>> visited(N, vector<bool>(N, false));
    visited[y][x] = true;

    while(!q.empty()) {
        auto [curY, curX] = q.front(); q.pop();

        for(int dir = 0; dir < 4; dir++) {
            int newY = curY + dr[dir];
            int newX = curX + dc[dir];

            if(newY < 0 || newX < 0 || newY >= N || newX >= N || visited[newY][newX])
                continue;

            visited[newY][newX] = true;

            if(grid[newY][newX].id == 0) {
                availableCells++;
                q.push({newY, newX});
            }
        }
    }

    return availableCells;
}

Result putBacteria(int mTime, int mRow, int mCol, Bacteria mBac) {
    curTime = mTime;
    removeExpiredBacteria(curTime);

    if (grid[mRow-1][mCol-1].id != 0) return {0, 0};

    int endTime = mTime + mBac.time;
    int cellsToOccupy = mBac.size;

    int availableCells = bfs(mRow-1, mCol-1);

    if(availableCells < mBac.size) return {0, 0};

    priority_queue<Cell> pq;
    pq.push({0, mRow, mCol});

    while (!pq.empty() && cellsToOccupy > 0) {
        auto current = pq.top(); pq.pop();

        if (grid[current.row-1][current.col-1].id != 0) continue;

        grid[current.row-1][current.col-1] = {mBac.id, endTime};
        cellsToOccupy--;

        if (cellsToOccupy == 0) {
            return {current.row, current.col};
        }

        for (int i = 0; i < 4; ++i) {
            int newRow = current.row + dr[i];
            int newCol = current.col + dc[i];
            int newDistance = abs(mRow - newRow) + abs(mCol - newCol);

            if (newRow >= 1 && newRow <= N && newCol >= 1 && newCol <= N &&
                grid[newRow-1][newCol-1].id == 0) {
                pq.push({newDistance, newRow, newCol});
            }
        }
    }
}


int killBacteria(int mTime, int mRow, int mCol) {
    curTime = mTime;

    if (grid[mRow-1][mCol-1].endTime <= curTime) {
        return 0;
    }
    int killedId = grid[mRow-1][mCol-1].id;
    if (killedId == 0) return 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (grid[i][j].id == killedId) {
                grid[i][j] = {0, 0};
            }
        }
    }
    return killedId;
}


int checkCell(int mTime, int mRow, int mCol) {
    curTime = mTime;

    if (grid[mRow-1][mCol-1].endTime <= curTime) {
        return 0;
    }
    return grid[mRow-1][mCol-1].id;
}