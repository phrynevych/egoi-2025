#include "validator.h"

void run() {
  int n = Int(2, Arg("maxn"));
  Space();
  int m = Int(Arg("minm",1), Arg("maxm"));
  Space();
  int k = Int(1, Arg("maxk"));
  Endl();

  int nm = int(Arg("max_nm", n*m));
  assert(n*m <= nm);

  for(int i = 0; i < n; i++){
    SpacedInts(m,0,k);
  }

  Eof();
}
