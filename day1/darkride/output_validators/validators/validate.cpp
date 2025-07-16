#include "validate.h"

#include <bits/stdc++.h>
using namespace std;

const int MAX_QUERIES = 30;

int main(int argc, char **argv) {
  init_io(argc, argv);

  is_sample = false;

  int N;
  judge_in >> N;
  vector<int> perm(N);
  for(int i = 0; i < N; ++i)
    judge_in >> perm[i];

  if(perm == vector<int>{2,1,0,3,4}) is_sample = true;
  if(perm == vector<int>{2,0,1})     is_sample = true;
  if(perm == vector<int>{0,1,2,3})   is_sample = true;

  if (is_sample) {
    tc_string = to_string(N) + "\n";
    for (int i = 0; i < N; i++) {
      if (i) tc_string += ' ';
      tc_string += to_string(perm[i]);
    }
  }

  cout << N << endl;
  if(is_sample) interaction += "<" + to_string(N) + "\n";

  int queries = 0;

  string line;
  auto readline = [&]() -> bool {
    if (!getline(cin, line)) return false;
    if (is_sample) interaction += ">" + line + "\n";
    return true;
  };

  auto read_in_range = [&](auto& iss) {
      int x;
      iss>>x;
      if(!iss) wrong_answer("unexpected eof");
      if(x < 0 || x >= N) wrong_answer("%d out of range", x);
      return x;
  };

  vector<int> marked_at_query(N, -9);

  char garbage;
  for (;;) {
    if (!readline()) wrong_answer("eof0");
    istringstream iss(line);

    char type;
    iss >> type;
    if(!iss) wrong_answer("unexpected eof1");
    if(type == '!') {
      int a = read_in_range(iss);
      int b = read_in_range(iss);
      if (iss >> garbage) wrong_answer("extra1");
      auto [pa, pb] = minmax(perm[a], perm[b]);
      if(pa != 0 || pb != N-1)
        wrong_answer("answer (%d,%d) maps to (%d,%d)", a, b, pa, pb);
      break; // answer okay
    }
    else if(type == '?') {
      ++queries;
      if(queries > MAX_QUERIES)
        wrong_answer("too many queries");
      vector<int> v;
      for(int i = 0; i < N; ++i) {
        char c;
        iss>>c;
        if(!iss) wrong_answer("unexpected eof3");
        if(c != '0' && c != '1')
          wrong_answer("[query %d] unexpected (char: \'%c\'; ascii: %d)",
                       queries, c, (int)c);
        if(c == '1') v.emplace_back(i);
      }
      if (iss >> garbage) wrong_answer("extra2");
      vector<int> todo;
      for(auto y : v) {
        int x = perm[y];
        if(marked_at_query[x] == queries)
          judge_error("duplicate switch, should not happen");
        marked_at_query[x] = queries;
        todo.push_back(x);
        if(x > 0) todo.push_back(x-1);
        if(x+1 < N) todo.push_back(x+1);
      }
      sort(begin(todo), end(todo));
      todo.erase(unique(begin(todo), end(todo)), end(todo));
      int changes = 0;
      for(int i = 0; i+1 < (int)size(todo); ++i) {
        int green1 = (marked_at_query[todo[i]] == queries);
        int green2 = (marked_at_query[todo[i+1]] == queries);
        if(green1 != green2) ++changes;
      }
      cout << changes << endl;
      if(is_sample) interaction += "<" + to_string(changes) + "\n";
    }
    else{
      wrong_answer("[query %d] bad query type (char: \'%c\'; ascii: %d)",
                   queries, type, (int)type);
    }
  }


  while (readline()) {
    if (!line.empty()) wrong_answer("trailing output, expected eof");
  }

  judge_message("used %d queries", queries);
  accept();
}
