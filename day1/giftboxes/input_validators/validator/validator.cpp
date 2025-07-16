#include "validator.h"

void run() {
  int n = Int(1, Arg("maxn"));
  Space();
  int m = Int(1, Arg("maxm"));
  if (n >= m) die_line("n >= m");
  Endl();

  string mode = Arg("mode", "");
  if (mode == "plusOne" && n+1 != m) die_line("m != n+1");
  if ((mode == "double" || mode == "doubleSort") && n*2 != m) die_line("m != n*2");

  vector<int> teams = SpacedInts(m, 0, n-1);
  vector<int> ppl(n, 0);
  for (int i = 0; i < (int)teams.size(); i++) {
    if (mode == "doubleSort" && i == (int)teams.size()/2) {
      for (int p: ppl) if (!p) die_line(to_string(p) + " does not exist in the first half");
    }
    ppl[teams[i]] += 1;
  }

  for (int i = 0; i < (int)ppl.size(); i++) {
    if (!ppl[i]) die_line(to_string(i) + " does not exist");
    if ((mode == "double" || mode == "doubleSort") && ppl[i] != 2) die_line(to_string(i) + " does not exist two times");
  }
  Eof();
}
