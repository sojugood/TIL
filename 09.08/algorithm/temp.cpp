#include <iostream>

using namespace std;

int main() {
	int temp = 0;
	for (int i = 0; i < 5; ++i) {
		int score;
		cin >> score;
		if (score < 40) {
			score = 40;
		}
		temp += score;
	}

	cout << temp / 5 << endl;
	return 0;
}