#include <bits/stdc++.h>

using namespace std;

int main() {
    int P, N;
    cin >> P >> N;
    if (P == 1) {
        vector<int> a(N - 1);
        vector<int> b(N - 1);
        for (int i = 0; i < N - 1; ++i) {
            cin >> a[i] >> b[i];
        }

        string message = "0101";
        vector<int> l(N - 1);

        cout << message << endl;
        for (int i = 0; i < N - 1; ++i) {
            cout << l[i] << endl;
        }
    } else {
        cin.ignore(100, '\n');
        string message;
        getline(cin, message);

        for (int i = 0; i < N - 1; ++i) {
            int a, b;
            cin >> a >> b;

            bool guess_a = true;

            if (guess_a) {
                cout << a << endl;
            } else {
                cout << b << endl;
            }
        }
    }
    return 0;
}
