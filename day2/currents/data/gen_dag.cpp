// first makes a line from 1 to N through every node
// then randomly adds edges on top of that, preserving the DAG property 

#include <iostream>
#include <random>
#include <cstdlib>
#include <cassert>
#include "graphlib.h"

using namespace std;

int N, M;

int main(int argc, char *argv[]) {
    int seed;
    assert(argc == 4);
    N = atoi(argv[1]);
    M = atoi(argv[2]);
    seed = atoi(argv[3]);
    assert (M >= N-1);

    srand(seed);

    set<pii> e;
    for(int i = 0; i < N-1; i++){
        e.insert({i, i+1});
    }

    for(int i = 0; i < M-(N-1); i++){
        int a, b;

        do
        {
            a = rng(0, N - 1)();
            b = rng(0, N - 1)();
            if(b < a) swap(a, b);
        }
        while(a == b or e.find(pii(a, b)) != e.end());
        e.insert(pii(a, b));
        
    }
    
    mt19937 g(seed);

    vector<pii> edges(e.begin(), e.end());
    shuffle(edges.begin(), edges.end(), g);
    vector<int> p = random_permutation(N-2, g);
    vector<int> m(N);
    m[0] = 0;
    m[N-1] = N-1;

    for(int i = 1; i < N-1; i++){
        m[i] = p[i-1] + 1; 
    }

    cout << N << " " << edges.size() << endl;

    for(auto [a, b] : edges){
        cout << m[a] << " " << m[b] << endl;
    }

    return 0;
}
