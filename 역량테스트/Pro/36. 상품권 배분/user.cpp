// user.cpp

#include <unordered_map>
#include <algorithm>

using namespace std;

// 각 부서를 저장하는 구조체
// root 부서는 최대 1000개, add 함수의 최대 호출 횟수 17000번
// 최대 part의 개수는 18000개
struct Part {
	int people_count;
	int my_parent;
	int child[3];
	int child_count;
}part[18001];

unordered_map<int, int> part_map;

int part_arr;

int n;

int sum_people;


void init(int N, int mId[], int mNum[]) {
	// 초기화
	n = N;
	part_arr = 1;
	part_map.clear();
	sum_people = 0;
	for (int i = 0; i < 18001; i++) {
		part[i] = { 0, -1, {0, 0, 0}, 0 };
	}

	for (int i = 0; i < n; i++) {
		part[part_arr].people_count = mNum[i];
		part[part_arr].my_parent = -1;
		part[part_arr].child_count = 0;
		part_map[mId[i]] = part_arr;
		part_arr++;

		sum_people += mNum[i];
	}
	return;
}

int add(int mId, int mNum, int mParent) {
	int parent_index = part_map[mParent];

	if (part[parent_index].child_count >= 3) {
		return -1;
	}

	part[part_arr].people_count = mNum;
	part[part_arr].my_parent = parent_index;
	part[part_arr].child_count = 0;
	part_map[mId] = part_arr;

	part[parent_index].child[part[parent_index].child_count++] = part_arr;
	part_arr++;

	int current_index = parent_index;
	while (current_index != -1) {
		part[current_index].people_count += mNum;
		current_index = part[current_index].my_parent;
	}

	sum_people += mNum;
	return part[parent_index].people_count;
}

void dfs(int idx) {
	for (int i = 0; i < part[idx].child_count; i++) {
		dfs(part[idx].child[i]);
	}
	int partId = -1;
	for (const auto& pair : part_map) {
		if (pair.second == idx) {
			partId = pair.first;
			break;
		}
	}
	if (partId != -1) {
		part_map.erase(partId);
	}
}

int remove(int mId) {
	if (part_map.find(mId) == part_map.end()) {
		return -1;
	}

	int idx = part_map[mId];
	int return_value = part[idx].people_count;
	int parent_index = part[idx].my_parent;

	for (int i = 0; i < part[parent_index].child_count; i++) {
		if (part[parent_index].child[i] == idx) {
			for (int j = i; j < part[parent_index].child_count - 1; j++) {
				part[parent_index].child[j] = part[parent_index].child[j + 1];
			}
			part[parent_index].child_count--;
			break;
		}
	}

	int current_index = parent_index;
	while (current_index != -1) {
		part[current_index].people_count -= return_value;
		current_index = part[current_index].my_parent;
	}

	dfs(idx);
	sum_people -= return_value;
	part_map.erase(mId);

	return return_value;
}

int distribute(int K) {
	if (sum_people <= K) {
		int max_value = -1;
		for (int i = 1; i < part_arr; i++) {
			max_value = max(max_value, part[i].people_count);
		}
		return max_value;
	}

	int left = 1, right = K;
	while (left <= right) {
		int mid = (left + right) / 2;
		int required_tickets = 0;

		for (int i = 1; i <= n; i++) {
			if (part[i].people_count <= mid) {
				required_tickets += part[i].people_count;
			}
			else {
				required_tickets += mid;
			}
		}

		if (required_tickets <= K) {
			left = mid + 1;
		}
		else {
			right = mid - 1;
		}
	}
	return right;
}
