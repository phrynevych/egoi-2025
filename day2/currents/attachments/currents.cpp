#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> a(M);
    vector<int> b(M);
    for (int i = 0; i < M; ++i) {
        cin >> a[i] >> b[i];
    }

    vector<int> ans(N - 1);

    for (int i = 0; i < N - 1; ++i) {
        cout << ans[i] << ' ';
    }
    cout << endl;

    return 0;
}
