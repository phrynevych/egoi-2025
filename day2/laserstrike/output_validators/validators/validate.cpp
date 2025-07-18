#include "validate.h"

#include <bits/stdc++.h>
using namespace std;

int main(int argc, char **argv) {
	init_io(argc, argv);

	// Hakeshake step. Technically this isn't necessary and this could be a
	// non-interactive problem (since our include/ takes care of interaction),
	// but it's nice to have it marked interactive in Kattis, and a handshake
	// might give slightly better error messages for non-C++/Python submissions.
	cout << "must_use_cpp_or_python" << endl;
	string auth;
	getline(cin, auth);
	if (!cin || auth != "NPMzpA53vMVb") {
		wrong_answer("must use C++ or Python include files (bad initial auth: %s)", auth.c_str());
	}

	string input;

	static char buf[1 << 20];
	while (judge_in.read(buf, sizeof(buf))) {
		input += string(buf, buf + sizeof(buf));
	}
	input += string(buf, buf + judge_in.gcount());

	cout.write(input.data(), input.size());
	cout.flush();

	is_sample = (input[0] == '1');
	if (is_sample) {
		tc_string = input.substr(2);
	}

	int K;
	auth = "eof from runner!?";
	getline(cin, auth);
	if (auth == "WA:zzxUGG46vWcg") {
		getline(cin, auth);
		string line;
		if (is_sample) {
			while (getline(cin, line))
				interaction += line + '\n';
		}
		cerr << "wrong answer: " << auth << endl;
		wrong_answer("wrong answer: %s\n", auth.c_str());
	}
	if (!cin || auth != "OK:LWWe75RrS4Vq") {
		cerr << "bad runner output, giving wrong answer: " << auth << endl;
		wrong_answer("bad runner output, giving wrong answer: %s\n", auth.c_str());
	}
	cin >> K;
	if (!cin) {
		wrong_answer("missing K!?");
	}

	int clampedK = max(K, 1);
	double score = 1.0 - 0.3 * log10(clampedK);

	// grader will rescale this to the test group's correct value
	score *= 1000;

	judge_message("used K = %d; score: %.2f", K, score);
	accept_with_score(score);
}
