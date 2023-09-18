#include <iostream>
#include <vector>
using namespace std;

int res;

vector<int> merge(const vector<int>& left, const vector<int>& right) {
    if (left.back() > right.back()) {
        res += 1;
    }

    vector<int> result;
    int i = 0, j = 0;

    while (i < left.size() && j < right.size()) {
        if (left[i] < right[j]) {
            result.push_back(left[i]);
            i++;
        } else {
            result.push_back(right[j]);
            j++;
        }
    }

    while (i < left.size()) {
        result.push_back(left[i]);
        i++;
    }

    while (j < right.size()) {
        result.push_back(right[j]);
        j++;
    }

    return result;
}

vector<int> merge_sort(const vector<int>& arr) {
    if (arr.size() <= 1) {
        return arr;
    }

    int mid = arr.size() / 2;
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());

    left = merge_sort(left);
    right = merge_sort(right);

    return merge(left, right);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
    int T;
    cin >> T;

    for (int tc = 1; tc <= T; ++tc) {
        int N;
        cin >> N;

        vector<int> arr(N);
        for (int i = 0; i < N; ++i) {
            cin >> arr[i];
        }

        res = 0;
        vector<int> sortedArr = merge_sort(arr);

        cout << "#" << tc << " " << sortedArr[N / 2] << " " << res << "\n";
    }

    return 0;
}
