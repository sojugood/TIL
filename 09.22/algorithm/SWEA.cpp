#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MAX_N = 1e5 + 1;

int parent[MAX_N];
int diff[MAX_N];
int Rank[MAX_N];

pair<int, int> find(int x) {
    if (x == parent[x]) {
        return { x, 0 };
    }
    auto[px, pd] = find(parent[x]);
    parent[x] = px;
    diff[x] += pd;
    return { parent[x], diff[x] };
}

void union_func(int a, int b, int w) {
    auto[pa, da] = find(a);
    auto[pb, db] = find(b);

    if (pa != pb) {
        if (Rank[pa] > Rank[pb]) {
            parent[pb] = pa;
            diff[pb] = da - db + w;
        } else {
            parent[pa] = pb;
            diff[pa] = db - da - w;
            if (Rank[pa] == Rank[pb]) {
                Rank[pb]++;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; ++tc) {
        int N, M;
        cin >> N >> M;

        for (int i = 1; i <= N; ++i) {
            parent[i] = i;
            diff[i] = 0;
            Rank[i] = 0;
        }

        vector<string> results;

        for (int i = 0; i < M; ++i) {
            string op;
            cin >> op;
            if (op == "!") {
                int a, b, w;
                cin >> a >> b >> w;
                union_func(a, b, w);
            } else {
                int a, b;
                cin >> a >> b;
                auto[pa, da] = find(a);
                auto[pb, db] = find(b);
                if (pa == pb) {
                    results.push_back(to_string(db - da));
                } else {
                    results.push_back("UNKNOWN");
                }
            }
        }

        cout << "#" << tc << " ";
        for (const auto& res : results) {
            cout << res << " ";
        }
        cout << "\n";
    }
    return 0;
}
