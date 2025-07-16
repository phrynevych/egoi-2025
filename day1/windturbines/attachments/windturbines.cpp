#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, M, Q;
    cin >> N >> M >> Q;

    vector<int> u(M);
    vector<int> v(M);
    vector<long long> c(M);
    for (int i = 0; i < M; ++i) {
        cin >> u[i] >> v[i] >> c[i];
    }

    vector<int> l(Q);
    vector<int> r(Q);
    for (int i = 0; i < Q; ++i) {
        cin >> l[i] >> r[i];
    }

    vector<long long> ans(Q, 0);

    for (int i = 0; i < Q; ++i) {
        cout << ans[i] << endl;
    }

    return 0;
}
