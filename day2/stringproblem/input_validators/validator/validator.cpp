#include "validator.h"

void run() {
  int n = Int(Arg("minn"), Arg("maxn"));
  Endl();

  string mode = Arg("mode", "");

  vector<pair<int, int>> hair(n);
  set<int> endpoints;
  for (int i = 0; i < n; i++) {
    int a = Int(0, 2 * n - 1);
    Space();
    int b = Int(0, 2 * n - 1);
    Endl();
    hair[i] = {a, b};
    endpoints.insert(a);
    endpoints.insert(b);
  }
  if (endpoints.size() != 2 * n) die("endpoints not unique");
  Eof();

  if (mode == "ans02") {
    map<int, int> countAngles;
    for (int i = 0; i < n; i++) countAngles[(hair[i].first + hair[i].second) % (2 * n)]++;
    for (auto x : countAngles) {
      if (x.first % 2 && (x.second == n - 2 || x.second == n)) return;
    }
    die("wrong number of ops needed");
  } else if (mode == "adjacent") {
    for (int i = 0; i < n; i++) {
      if (hair[i] != make_pair(2 * i, 2 * i + 1) && hair[i] != make_pair(2 * i + 1, 2 * i)) die("hair " + to_string(i) + " does not connect adjacent endpoints");
    }
  } else if (mode == "star") {
    for (int i = 0; i < n; i++) {
      if (hair[i] != make_pair(i, i + n) && hair[i] != make_pair(i + n, i)) die("hair " + to_string(i) + " does not connect opposite endpoints");
    }
  } else if (mode == "angle1") {
    vector<int> countAngles(2 * n, 0);
    for (int i = 0; i < n; i++) countAngles[(hair[i].first + hair[i].second) % (2 * n)]++;
    for (int i = 0; i < 2 * n; i++) {
      if (i % 2 == 1 && countAngles[i] > countAngles[1]) die("angle " + to_string(i) + " appears more often than angle 1");
    }
  } else {
    assert(mode == "");
  }
}
