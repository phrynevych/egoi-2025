#include "validate.h"
#include <vector>
#include <set>
using namespace std;

int main(int argc, char **argv) {
  init_io(argc, argv);

  int n, m;
  judge_in >> n >> m;

  int startAuthor, endAuthor, startJudge, endJudge;
  if (!(author_out >> startAuthor)) wrong_answer("no output");
  judge_ans >> startJudge;

  if (!(author_out >> endAuthor)) wrong_answer("only one number printed");
  judge_ans >> endJudge;

  if (endAuthor < startAuthor || startAuthor < 0 || endAuthor < 0 || startAuthor >= m || endAuthor >= m) wrong_answer("%d and %d are invalid ids", startAuthor, endAuthor);
  if (endAuthor-startAuthor != endJudge-startJudge) wrong_answer("%d instead of %d people skipped", endJudge-startJudge+1, endAuthor-startAuthor+1);

  vector<int> ppl(m);
  for (int i = 0; i < m; i++) judge_in >> ppl[i];
  
  set<int> gifted;
  for (int i = 0; i < m; i++) {
    if (i < startAuthor || i > endAuthor) gifted.insert(ppl[i]);
  }

  if (static_cast<int>(gifted.size()) != m-(endJudge-startJudge+1)) wrong_answer("only %d instead of %d teams received their gift", static_cast<int>(gifted.size()), m-(endJudge-startJudge+1));

  string x;
  if (author_out >> x) wrong_answer("eof expected");
  accept();
}
