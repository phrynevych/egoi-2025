// first builds two random spanning trees, one for 1 and one for N
// Then adds M_add random edges, or adds edges until M_max is reached

#include <iostream>
#include <random>
#include <cstdlib>
#include <cassert>
#include "graphlib.h"

using namespace std;

int N, M_add, M_max;
bool is_sub;

void root_tree(graph& tree, int root, int par, set<pii>& e, bool rev) {
    for(int child: tree[root]){
        if(child == par) continue;
        if (rev)
            e.insert({child, root});
        else
            e.insert({root, child});
        root_tree (tree, child, root, e, rev);
    }
}

int main(int argc, char *argv[]) {
    int seed;
    assert(argc == 6);
    N = atoi(argv[1]);
    M_add = atoi(argv[2]);
    M_max = atoi(argv[3]);
    is_sub = atoi(argv[4]);
    seed = atoi(argv[5]);

    srand(seed);

    graph tree1(N);
    tree1 = random_tree(N);

    set<pii> e;
	root_tree(tree1, 0, -1, e, false);

    if(is_sub){
        for(int i = 0; i < N-1; i++)
        e.insert({i, N-1});
    }
    else{
        graph treeN(N);
        treeN = random_tree(N);
        root_tree(treeN, N-1, -1, e, true);
    }

    assert (M_max >= (int)e.size() && "M too small");

    for(int i = 0; i < min(M_max - (int)e.size(), M_add); i++){
        int a, b;

        do
        {
            a = rng(0, N - 1)();
            b = rng(0, N - 1)();
        }
        while(a == b or e.find(pii(a, b)) != e.end());
        e.insert(pii(a, b));
        
    }

    mt19937 g(seed);
    
    vector<pii>edges(e.begin(), e.end());
    shuffle(edges.begin(), edges.end(), g);

    cout << N << " " << e.size() << endl;

    for(auto [a, b] : e){
        cout << a << " " << b << endl;
    }

    return 0;
}
