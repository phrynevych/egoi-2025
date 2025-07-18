#include <iostream>
#include <random>
#include <cstdlib>
#include <cassert>
#include "graphlib.h"

using namespace std;

int N;

int main(int argc, char *argv[]) {
    int seed;
    assert(argc == 3);
    N = atoi(argv[1]);
    seed = atoi(argv[2]);

    srand(seed);

    set<pii> e;
    for(int i = 0; i < N-1; i++){
        e.insert({i, i+1});
    }

    e.insert({0, N-3});
    
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
