#include "validator.h"
#include <bits/stdc++.h>
using namespace std;


void dfs(int v, vector<int>& vis, vector<vector<int>>& adj){
  if(vis[v]) return;
  vis[v] = 1;
  for(int u:adj[v]){
    dfs(u,vis,adj);
  }
}

void run() {
  int n = Int(2, Arg("maxn"));
  Space();
  int m = Int(1,Arg("maxm"));
  Space();
  int q = Int(1,Arg("maxq"));
  Endl();
  long long maxw = (long long)Arg("maxw");
  set<pair<int,int>> e;

  bool isPath = Arg("path", false);
  bool isLeft = Arg("left", false);
  bool isTuple = Arg("tuple", false);

  string mode = Arg("mode","");
  vector<int> seen(n-1,0);
  vector<int> vis(n,0);
  vector<vector<int>> adj(n);
  for(int i=0;i<m;++i){
    int u = Int(0,n-1);
    Space();
    int v = Int(0,n-1);
    assert(u!=v);
    assert(e.find({u,v})==e.end());
    e.insert({u,v});
    e.insert({v,u});
    adj[v].push_back(u);
    adj[u].push_back(v);
    Space();
    long long w = Int(1,maxw);
    Endl();
    if (isPath) {
        assert(u==i);
        assert(v == i+1);
        seen[u]=1;
    }
  }
  dfs(0,vis,adj);
  assert(accumulate(vis.begin(),vis.end(),0)==n);
  if (isPath) assert(accumulate(seen.begin(),seen.end(),0)==n-1);
  long long sum = 0;
  for(int i=0;i<q;++i) {
    int l = Int(0,n-1);
    Space();
    int r = Int(0,n-1);
    Endl();
    sum += (r-l+1);
    assert(l <= r);
    
    if (isLeft) assert(l==0);
    if (isTuple) assert(r==l+1);
  }
  
  assert(sum <= (long long)Arg("maxs"));
}
