#include "validate.h"
#include <bits/stdc++.h>
using namespace std;

const int k = 12;
const int m = 50;
using bs = bitset<m>;

int main(int argc, char **argv) {
  init_io(argc, argv);

  int n;
  judge_in >> n;

  auto check = [&](auto& solution_out, auto& fail) {
    vector<bs> tickets(n);
    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < k; ++j) {
        int x;
        if(!(solution_out >> x))
          fail("not enough numbers in output");
        if(!(0 <= x && x < m))
          fail("%d not in [0,%d)", x, m);
        if(tickets[i][x] == 1)
          fail("%d seen twice in ticket %d", x, i);
        tickets[i][x] = 1;
      }
    }

    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < i; ++j) {
        if(tickets[i] == tickets[j])
          fail("tickets %d and %d are the same", i, j);
        bs overlap = tickets[i] | tickets[j];
        for(int b = 0; b < m; ++b) if(overlap[b]) {
          // Could b be the last number drawn to make both
          // tickets i and j win simultaneously?
          // If not, must exist another $ticket \subseteq overlap \setminus \{b\}$)
          bs taken = overlap;
          taken[b] = 0;
          bool ok = false;
          for(int i = 0; i < n; ++i) {
            if((tickets[i] | taken) == taken) { // "tickets[i] \subseteq taken"
              ok = true;
              break;
            }
          }
          if(!ok)
            fail("tickets %d and %d can finish using %d", i,j,b);
        }
      }
    }

    string garbage;
    solution_out >> garbage;
    if(solution_out) fail("trailing output, expected eof");
  };

  check(author_out, wrong_answer);
  check(judge_ans, judge_error); // TODO: comment out to speed up?

  accept();
}
