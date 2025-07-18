#include "validator.h"
#include <bits/stdc++.h>

using namespace std;

// returns if cycle found
// vis[i] = 0 -> unvis, vis[i] = 1 -> in process, vis[i] = 2 -> vis
bool dfs(int node, vector<vector<int>>& adj, vector<int>& vis){
    bool cycle = (vis[node] == 1);
    if(vis[node] != 0) return cycle;
    vis[node] = 1;
    for(int ne: adj[node]){
        cycle = dfs(ne, adj, vis) || cycle;
    }

    vis[node] = 2;
    return cycle;
}

void run(){
    int N = Int(2, Arg("maxn"));
    Space();
    int M = Int(1, Arg("maxm"));
    bool acyclic = Arg("acyclic");
    bool line = Arg("line");
    bool all_to_N = Arg("all_to_N");
    Endl();

    vector<vector<int>> adj(N);
    vector<vector<int>> adj_rev(N);
    set<pair<int,int>> edges;

    for(int i = 0; i < M; i++){
        int a = Int(0, N-1);
        Space();
        int b = Int(0, N-1);
        if (a == b)
            die("self-loop found");
        if (edges.find({a,b}) != edges.end())
            die("edge duplication");

        Endl();

        if(line) {
            assert(a == i);
            assert(b == i + 1);
        }

        edges.insert({a,b});
        adj[a].push_back(b);
        adj_rev[b].push_back(a);
    }

    if(all_to_N){
        for(int i = 0; i < N-1; i++){
            if(edges.find({i, N-1}) == edges.end())
                die("not every node has an edge to N");
        }
    }

    //Check if everything is reachable from 0 and if cycle exists
    vector<int> vis(N, 0);
    bool cycle = dfs(0, adj, vis);
    if(acyclic && cycle) die("cycle found");
    for(int i = 0; i < N; i++){
        if(vis[i] == 0) die("not every node reachable from 0");
    }

    // Check if everything can reach N
    vector<int> vis2(N, 0);
    dfs(N-1, adj_rev, vis2);
    for(int i = 0; i < N; i++){
        if(vis2[i] == 0) die("not every node can reach N-1");
    }

}
