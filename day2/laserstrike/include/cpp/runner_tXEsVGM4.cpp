#include <string>
#include <cassert>
#include <sstream>
#include <vector>
#include <set>
#include <algorithm>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <sys/types.h>

#define CHECK(var, fn) do { if ((var) == -1) { perror(fn); exit(1); } } while (false)

using namespace std;

typedef pair<int, int> pii;

namespace {

bool is_sample;
string interaction;
const char* WA_MESSAGE = "WA:zzxUGG46vWcg";

int realStdout;

void writeToFd(int fd, const string& buf) {
	const char* ptr = buf.data();
	size_t len = buf.size();
	while (len > 0) {
		ssize_t w = write(fd, ptr, len);
		if (w == -1 && errno == EINTR) continue;
		if (w == -1 && errno == EPIPE) break;
		CHECK(w, "write");
		len -= w;
		ptr += w;
	}
}

[[noreturn]]
void printAndExit(const string& msg) {
	writeToFd(realStdout, msg);
	exit(0);
}

[[noreturn]]
void fail(string msg) {
	auto ind = msg.find('\n');
	if (ind != string::npos) msg = msg.substr(0, ind);
	printAndExit(string(WA_MESSAGE) + "\n" + msg + "\n" + interaction);
}

int parseInt(const string& s, const char* what, int lo, int hi) {
	// parse a base-10 number, ignoring leading/trailing spaces
	istringstream iss(s);
	int ret;
	string more;
	if (!(iss >> ret) || (iss >> more)) {
		fail(string("failed to parse ") + what + " as integer: " + s);
	}
	if (!(lo <= ret && ret <= hi)) {
		fail(string(what) + " out of bounds: " + to_string(ret) +
				" not in [" + to_string(lo) + ", " + to_string(hi) + "]");
	}
	return ret;
}

struct Reader {
	string buf;
	bool eof = false;
	size_t bufPos = 0;
	int fd;

public:
	Reader(int fd) : fd(fd) {}
	Reader(const Reader&) = delete;
	Reader(Reader&&) = default;

	string readLine() {
		// If we have a buffered line, return it.
		size_t ind = buf.find('\n', bufPos);
		if (ind != string::npos) {
			size_t oldPos = bufPos;
			bufPos = ind + 1;
			return string{buf.begin() + oldPos, buf.begin() + bufPos};
		}
		// Otherwise, discard stale parts of the buffer and read data until we
		// get a full line.
		buf.erase(buf.begin(), buf.begin() + bufPos);
		bufPos = 0;

		if (eof) return "";
		for (;;) {
			size_t searchStart = buf.size();
			static char readbuf[1 << 20];
			ssize_t r = read(fd, readbuf, sizeof(readbuf));
			if (r == -1 && errno == EINTR) continue;
			if (r == 0) {
				eof = true;
				ind = buf.size();
				break;
			}
			CHECK(r, "read");
			buf.insert(buf.end(), readbuf, readbuf + r);
			ind = buf.find('\n', searchStart);
			if (ind != string::npos) {
				ind++;
				break;
			}
		}
		bufPos = ind;
		return string{buf.begin(), buf.begin() + ind};
	}
};

struct Submission {
	int pid;
	int outFd;
	Reader fin;

	void wait() {
		int status;
		CHECK(waitpid(this->pid, &status, 0), "waitpid");
		if (WIFSIGNALED(status)) {
			// propagate the signal, or if not possible at least exit with an error
			writeToFd(1, "got signal " + to_string(status));
			CHECK(kill(getpid(), WTERMSIG(status)), "kill");
			exit(1);
		}
		int ex = WEXITSTATUS(status);
		if (ex != 0) {
			writeToFd(1, "got exit code " + to_string(ex));
			exit(ex);
		}
	}

	string readLine(const char* what) {
		string ret = this->fin.readLine();
		if (ret.empty()) {
			this->wait();
			fail(string("Failed to read ") + what + ": no more output");
		}
		if (ret.back() == '\n')
			ret.pop_back();
		if (is_sample) interaction += '>' + ret + '\n';
		return ret;
	}

	void write(const string& s) {
		if (is_sample) interaction += '<' + s;
		writeToFd(this->outFd, s);
	}
};

[[noreturn]]
void doRunSubmission(int in, int out) {
	CHECK(dup2(in, 0), "dup2");
	CHECK(dup2(out, 1), "dup2");
	// Throw an exception to resume execution at the end of real_main(),
	// after which main() will be called.
	throw true;
}

template<typename F>
void runSubmission(const F& callback) {
	int pipefds[2];
	CHECK(pipe(pipefds), "pipe");
	int c2pRead = pipefds[0], c2pWrite = pipefds[1];
	CHECK(pipe(pipefds), "pipe");
	int p2cRead = pipefds[0], p2cWrite = pipefds[1];
	pid_t pid = fork();
	CHECK(pid, "fork");

	if (pid == 0) {
		CHECK(close(c2pRead), "close");
		CHECK(close(p2cWrite), "close");
		signal(SIGPIPE, SIG_DFL);

		doRunSubmission(p2cRead, c2pWrite);
	} else {
		CHECK(close(p2cRead), "close");
		CHECK(close(c2pWrite), "close");

		Submission sub{pid, p2cWrite, Reader{c2pRead}};
		callback(sub);

		string remainder = sub.fin.readLine();
		if (!remainder.empty()) {
			if (is_sample) interaction += '>' + remainder + '\n';
			fail("Unexpected trailing output: " + remainder);
		}

		CHECK(close(c2pRead), "close");
		CHECK(close(p2cWrite), "close");

		sub.wait();
	}
}

__attribute__((constructor))
void real_main() try {
	const char* HANDSHAKE_REQ = "must_use_cpp_or_python";
	const char* HANDSHAKE_RESP = "NPMzpA53vMVb";
	const char* ACCEPTED_MSG = "OK:LWWe75RrS4Vq";

	signal(SIGPIPE, SIG_IGN);

	Reader stdin{0};
	assert(stdin.readLine() == HANDSHAKE_REQ + string("\n"));
	writeToFd(1, HANDSHAKE_RESP + string("\n"));

	{
		string inp = stdin.readLine(); // is_sample
		istringstream judgeIn(inp);
		judgeIn >> is_sample;
	}
	string inp = stdin.readLine(); // N
	istringstream judgeIn(inp);

	int N;
	judgeIn >> N;
	assert(judgeIn);

	inp.clear();
	for (int i = 0; i < N-1; i++) {
		inp += stdin.readLine(); // tree edge
	}

	vector<pii> fullTree;
	set<pii> fullTreeSet;
	judgeIn.str(inp);
	for (int i = 0; i < N-1; i++) {
		int a, b;
		judgeIn >> a >> b;
		assert(judgeIn);
		fullTree.push_back({a, b});
		fullTreeSet.insert({a, b});
	}

	// send stdout to stderr for the user program
	realStdout = dup(1);
	CHECK(realStdout, "dup");
	CHECK(dup2(2, 1), "dup2");

	// redirect the stdin fd to make it slightly harder to read stdin twice
	CHECK(close(0), "close");
	CHECK(open("/dev/null", O_RDONLY), "open");

	vector<pii> commEdges;
	vector<string> commStr;
	string helpStr;

	runSubmission([&](Submission& sub) {
		string staticInput = "1 " + to_string(N) + "\n";
		for (int i = 0; i < N-1; i++) {
			staticInput += to_string(fullTree[i].first);
			staticInput += " ";
			staticInput += to_string(fullTree[i].second);
			staticInput += "\n";
		}
		sub.write(staticInput);

		helpStr = sub.readLine("help string");
		for (char c : helpStr) {
			if (c != '0' && c != '1')
				fail("help is not a binary string: " + helpStr);
		}
		if (helpStr.size() > 1000)
			fail("help string is too long");

		vector<int> deg(N);
		vector<int> adjXor(N);
		for (auto& pa : fullTree) {
			deg[pa.first]++;
			deg[pa.second]++;
			adjXor[pa.first] ^= pa.second;
			adjXor[pa.second] ^= pa.first;
		}

		string astr, bstr;
		for (int i = 0; i < N - 1; i++) {
			string line = sub.readLine("node index");
			int a = parseInt(line, "node index", 0, N-1);
			if (deg[a] != 1)
				fail("must remove a leaf node in each stage");
			int b = adjXor[a];
			deg[a]--;
			deg[b]--;
			adjXor[a] ^= b;
			adjXor[b] ^= a;
			commEdges.push_back({a, b});
			if (!fullTreeSet.count({a, b})) swap(a, b);
			assert(fullTreeSet.count({a, b}));
			commStr.push_back(to_string(a) + " " + to_string(b) + "\n");
		}
	});

	runSubmission([&](Submission& sub) {
		sub.write("2 " + to_string(N) + "\n" + helpStr + "\n");

		for (int i = 0; i < N - 1; i++) {
			sub.write(commStr[i]);
			string line = sub.readLine("guessed index");

			auto& pa = commEdges[i];
			int a = pa.first, b = pa.second;
			int x = parseInt(line, "guessed index", 0, N-1);
			if (x != a && x != b)
				fail("guessed a vertex that was not an endpoint");
			if (x != a)
				fail("guessed the wrong vertex");
		}
	});

	printAndExit(string(ACCEPTED_MSG) + "\n" + to_string(helpStr.size()));

	assert(0);
} catch (bool) {}

}
