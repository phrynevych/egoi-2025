#include <iostream>
#include <random>
#include <cstdlib>
#include <cassert>
#include "randlib.h"

using namespace std;

int N;

int main(int argc, char *argv[]) {
    int seed;
    assert(argc == 3);
    N = atoi(argv[1]);
    seed = atoi(argv[2]);

    srand(seed);

    vector<pair<int,int> > edges;
    for(int i = 0; i < N-1; i++){
        edges.push_back({i, i+1});
    }
    
    cout << N << " " << (N-1) << endl;

    for(auto [a, b] : edges){
        cout << a << " " << b << endl;
    }

    return 0;
}
