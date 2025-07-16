#include "validator.h"
#include <bits/stdc++.h>
using namespace std;

void run() {
  int n = Int(3, Arg("maxn"));
  Endl();
  auto v = SpacedInts(n, 0, n-1);
  AssertUnique(v);
  if(Arg("first",0) && v[0] != 0)
    die_line("v[0] != 0");
  if(Arg("half",0)) {
    if(n%2 != 0) die_line("not even");
    int a = find(begin(v),end(v),0)-begin(v);
    int b = find(begin(v),end(v),n-1)-begin(v);
    if(a > b) swap(a,b);
    if(!(a < n/2 && n/2 <= b)) die_line("not split by halfs");
  }
  Eof();
}
