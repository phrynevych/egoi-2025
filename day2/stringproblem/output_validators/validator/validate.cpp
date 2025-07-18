#include "validate.h"
#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
using namespace std;

int main(int argc, char **argv) {
  init_io(argc, argv);

  int n;
  judge_in >> n;

  vector<vector<int>> strings(n, {0, 0});
  for (int i = 0; i < n; i++) {
    judge_in >> strings[i][0];
    judge_in >> strings[i][1];
  }

  int kAuthor, kJudge;
  author_out >> kAuthor;
  judge_ans >> kJudge;
  if (!author_out) wrong_answer("output too small");
  if (kAuthor < 0) wrong_answer("negative number of operations");

  auto wrong_answer = [&](const char* msg, ...) {
    if (kAuthor == kJudge) {
      accept_with_score(500);
    }
    va_list pvar;
    va_start(pvar, msg);
    vreport_feedback(FILENAME_JUDGE_MESSAGE, msg, pvar);
    exit(EXITCODE_WA);
  };

  int h, s, e;
  for (int i = 0; i < kAuthor; i++) {
    if(!(author_out >> h >> s >> e)) wrong_answer("output too small");
    if(h < 0 || h >= n) wrong_answer("%d invalid string id", h);
    if(s < 0 || s >= 2 * n) wrong_answer("%d invalid endpoint", s);
    if(e < 0 || e >= 2 * n) wrong_answer("%d invalid endpoint", e);

    if (strings[h][0] == s) strings[h][0] = e;
    else if (strings[h][1] == s) strings[h][1] = e;
    else wrong_answer("%d not an endpoint of string %d", s, h);
  }

  set<int> endpoints;
  int sum = (strings[0][0] + strings[0][1]) % (2 * n);
  for (int i = 0; i < n; i++) {
    endpoints.insert(strings[i][0]);
    endpoints.insert(strings[i][1]);
    if ((strings[i][0] + strings[i][1]) % (2 * n) != sum) wrong_answer("string %d and string 0 are not parallel", i);
  }
  if ((int)endpoints.size() != 2 * n) wrong_answer("only %d endpoints are used", (int)endpoints.size());


  if (kAuthor > kJudge) wrong_answer("%d instead of %d operations", kAuthor, kJudge);
  if (kAuthor < kJudge) judge_error("only %d operations used, judge uses %d operations", kAuthor, kJudge);

  string x;
  if (author_out >> x) wrong_answer("eof expected");

  accept_with_score(1000);
}
