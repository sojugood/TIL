#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	int T;
    cin >> T;

    for (int tc = 1; tc <= T; ++tc) {

        int N, M;
        cin >> N >> M;

        vector<int> ans(M);
        vector<vector<int>> arr(N, vector<int>(M));

        for (int i = 0; i < M; ++i) {
            cin >> ans[i];
        }
        
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                cin >> arr[i][j];
            }
        }

        int max_res = 0;
        int min_res = INT8_MAX;
        
        for (int i = 0; i < N; ++i) {

            int score = 0;
            int bonus = 1;

            for (int j = 0; j < M; ++j) {
                if (arr[i][j] == ans[j]) {
                    score += bonus;
                    bonus += 1;
                } else {
                    bonus = 1;
                }
            }

            max_res = max(max_res, score);
            min_res = min(min_res, score);
        }

        int result = max_res - min_res;
        cout << "#" << tc << " " << result << endl;
    }

    return 0;    
}
