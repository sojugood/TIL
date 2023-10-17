// main.cpp

#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

#include <vector>
#include <set>

using namespace std;

vector<int> arr;


void init(int N) {
	arr.clear();
	arr.resize(N + 1, 0);
	return;
}

int add(int mId, int mSize) {
	int res = 0;
	int cnt = 0;
	int last;
	for (int i = 1; i < arr.size(); ++i) {
		if (arr[i] == 0) {
			++cnt;
		}
		if (cnt == mSize) {
			last = i + 1;
			break;
		}
	}
	if (cnt < mSize) return -1;
	for (int i = 1; i < last; ++i) {
		if (arr[i] == 0) {
			if (res == 0) {
				res = i;
			}
			arr[i] = mId;
			mSize--;
		}
		if (mSize == 0) {
			break;
		}
	}
	return res;
}

int remove(int mId) {
	int tmp = 0;
	int res = 1;
	for (int i = 1; i < arr.size(); ++i) {
		if (arr[i] == mId) {
			if (tmp == 0) {
				tmp = i;
			}
			if (tmp != i) {
				tmp = i;
				++res;
			}
			arr[i] = 0;
			++tmp;
		}
	}
	return res;
}

int count(int mStart, int mEnd) {
	set<int> res;
	for (int i = mStart; i <= mEnd; ++i) {
		if (arr[i] != 0) {
			res.insert(arr[i]);
		}
	}
	return res.size();
}

#define CMD_INIT 1
#define CMD_ADD 2
#define CMD_REMOVE 3
#define CMD_COUNT 4

static bool run() {
	int q;
	scanf("%d", &q);

	int mid, msize, mstart, mend, n;
	int cmd, ans, ret = 0;
	bool okay = false;

	for (int i = 0; i < q; ++i) {
		scanf("%d", &cmd);
		switch (cmd) {
		case CMD_INIT:
			scanf("%d", &n);
			init(n);
			okay = true;
			break;
		case CMD_ADD:
			scanf("%d %d %d", &mid, &msize, &ans);
			ret = add(mid, msize);
			if (ans != ret)
				okay = false;
			break;
		case CMD_REMOVE:
			scanf("%d %d", &mid, &ans);
			ret = remove(mid);
			if (ans != ret)
				okay = false;
			break;
		case CMD_COUNT:
			scanf("%d %d %d", &mstart, &mend, &ans);
			ret = count(mstart, mend);
			if (ans != ret)
				okay = false;
			break;
		default:
			okay = false;
			break;
		}
	}
	return okay;
}

int main() {
	setbuf(stdout, NULL);
	freopen("sample_input.txt", "r", stdin);

	int T, MARK;
	scanf("%d %d", &T, &MARK);

	for (int tc = 1; tc <= T; tc++) {
		int score = run() ? MARK : 0;
		printf("#%d %d\n", tc, score);
	}

	return 0;
}