#include "validator.h"
#include <vector>
using namespace std;

struct UF {
	vector<int> e;
	UF(int n) : e(n, -1) {}
	bool sameSet(int a, int b) { return find(a) == find(b); }
	int size(int x) { return -e[find(x)]; }
	int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
	bool join(int a, int b) {
		a = find(a), b = find(b);
		if (a == b) return false;
		if (e[a] > e[b]) swap(a, b);
		e[a] += e[b]; e[b] = a;
		return true;
	}
};

vector<vector<int>> adj;
int dfs(int at, int par) {
	int depth = 0;
	for (int x : adj[at]) if (x != par) {
		depth = max(depth, dfs(x, at) + 1);
	}
	return depth;
}

void run() {
	int narg = Arg("n");
	assert(narg >= 3);
	Int(0, 1);
	Endl();
	int n = Int(narg, narg);
	Endl();
	UF uf(n);
	adj.resize(n);
	for (int i = 0; i < n-1; i++) {
		int a = Int(0, n-1);
		Space();
		int b = Int(0, n-1);
		Endl();
		assert(a < b);
		assert(uf.join(a, b));
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	vector<int> degc(n);
	for (int i = 0; i < n; i++) {
		degc[adj[i].size()]++;
	}
	if (Arg("line", 0)) {
		assert(degc[1] == 2);
		assert(degc[2] == n-2);
	}
	if (Arg("star", 0)) {
		assert(degc[1] == n-1);
		assert(degc[n-1] == 1);
	}
	if (Arg("linestar", 0)) {
		assert(degc[1] + degc[2] == n-1);
	}
	int maxdiam = Arg("maxdiameter", -1);
	if (maxdiam != -1) {
		int diam = 0;
		for (int i = 0; i < n; i++) {
			diam = max(diam, dfs(i, -1));
		}
		if (diam > maxdiam) {
			die("Diameter " + to_string(diam) + " is greater than max of " + to_string(maxdiam));
		}
	}
}
