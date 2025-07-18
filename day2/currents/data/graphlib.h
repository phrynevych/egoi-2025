#ifndef GRAPHLIB_H_INCLUDED
#define GRAPHLIB_H_INCLUDED

#include <cstdio>
#include <set>
#include <tuple>

#include "randlib.h"

typedef std::pair<int, int> pii;

class graph
{
 public:
    graph(FILE *fin, bool directed = false) : _directed(directed)
    {
        int N, M; fscanf(fin, "%d %d", &N, &M);
        adj.resize(N);

        for(int i = 0; i < M; ++i)
        {
            int a, b; fscanf(fin, "%d %d", &a, &b);
            --a; --b;
            add_edge(a, b);
        }
    }

    graph(int N, bool directed = false) : adj(N), _num_edges(0), _directed(directed)
    {}

    void add_node()
    {
        adj.push_back(std::vector<int>());
    }

    void add_edge(int a, int b)
    {
        ++_num_edges;
        adj[a].push_back(b);
        if(not _directed and a != b) adj[b].push_back(a);
    }

    int append(const graph &g)
    {
        int x = num_nodes();

        for(int v = 0; v < g.num_nodes(); ++v)
        {
            add_node();
            for(int w : g[v]) adj[x + v].push_back(x + w);
        }

        _num_edges += g._num_edges;

        return x;
    }

    int num_nodes() const { return (int)adj.size(); }
    int num_edges() const { return _num_edges; }

    std::vector<int> & operator[](int i)
    {
        return adj[i];
    }

    const std::vector<int> & operator[](int i) const
    {
        return adj[i];
    }

    std::set<std::pair<int, int>> edges() const
    {
        std::set<std::pair<int, int>> result;
        for (int i = 0; i < num_nodes(); ++i) {
            for (int j: adj[i]) {
                if (!_directed && i > j) result.emplace(j, i);
                else result.emplace(i, j);
            }
        }
        return result;
    }

    void shuffle(std::mt19937 g)
    {
        std::vector<int> permutation = random_permutation(num_nodes(), g);
        adj = permute(adj, inverse_permutation(permutation));

        for(size_t i = 0; i < adj.size(); ++i)
            adj[i] = pick(adj[i], permutation);

        for(size_t i = 0; i < adj.size(); ++i)
        {
            permutation = random_permutation((int)adj[i].size(), g);
            adj[i] = permute(adj[i], permutation);
        }
    }

    void write(FILE *fout, bool shuffle = false, bool print_num_edges = true, bool print_num_nodes = true)
    {
        if(print_num_nodes) fprintf(fout, "%d", num_nodes());
        if(print_num_edges) fprintf(fout, " %d", num_edges());
        if(print_num_nodes or print_num_edges) fprintf(fout, "\n");

        std::vector<pii> edges;

        for(size_t i = 0; i < adj.size(); ++i)
            for(size_t j = 0; j < adj[i].size(); ++j)
                if(_directed or static_cast<int>(i) <= adj[i][j])
                    edges.push_back(pii(i + 1, adj[i][j] + 1));

        //if(shuffle)
        //{
        //    rand_shuffle(edges.begin(), edges.end());
        //}

        for(size_t i = 0; i < edges.size(); ++i)
        {
            if(not shuffle or prob(.5)) fprintf(fout, "%d %d\n", edges[i].first, edges[i].second);
            else                        fprintf(fout, "%d %d\n", edges[i].second, edges[i].first);
        }
    }

 private:
    std::vector<std::vector<int>> adj;
    int _num_edges;
    bool _directed;
};

/*
 * Construct a random tree with N nodes using Prufer codes
 */
graph random_tree(int N)
{
    graph g(N);

    std::vector<int> prufer(N - 2);
    generate(prufer.begin(), prufer.end(), rng(0, N - 1));

    /*std::vector<int>  s(N, 0);
    std::vector<bool> t(N, false);
    for(int i = 0; i < prufer.size(); ++i) ++s[prufer[i]];

    int counter = 0;

    for(int i = 0; i < prufer.size(); ++i)
    {
        while(s[counter]) ++counter;

        if(counter >= N)
            throw "implementation error in random_tree";

        ++s[counter]; --s[prufer[i]];
        if(s[prufer[i]] == 0) counter = min(counter, prufer[i]);
        t[counter] = true;
        g.add_edge(prufer[i], counter);
    }*/
    std::vector<bool> t(N, false);
    std::vector<int> forbidden(N, 0);
    for(size_t i = 0; i < prufer.size(); ++i) ++forbidden[prufer[i]];

    std::set<int> allowed;
    for(size_t i = 0; i < forbidden.size(); ++i)
        if(not forbidden[i]) allowed.insert((int)i);

    for(size_t i = 0; i < prufer.size(); ++i)
    {
        if(allowed.empty())
            throw "implementation error in random_tree";

        int w = *allowed.begin();
        allowed.erase(w);

        ++forbidden[w]; t[w] = true;
        --forbidden[prufer[i]];

        if(forbidden[prufer[i]] == 0)
            allowed.insert(prufer[i]);

        g.add_edge(prufer[i], w);
    }

    std::vector<int> rem;

    for(int i = 0; i < N; ++i)
        if(not t[i]) rem.push_back(i);

    if(rem.size() != 2)
        throw "implementation error in random_tree";

    g.add_edge(rem[0], rem[1]);
    return g;
}

/* Construct a "random" connected graph with N nodes and M edges
 * CAUTION: This algorithm is biased towards graphs with many spanning trees
 * (probably there is no quasilinear algorithm for this)
 */
graph random_graph(int N, int M)
{
    graph g = random_tree(N);

    std::set<pii> edges;
    for(int i = 0; i < N; ++i)
    {
        for(size_t j = 0; j < g[i].size(); ++j)
        {
            edges.insert(pii(i, g[i][j]));
            edges.insert(pii(g[i][j], i));
        }
    }

    for(int i = N - 1; i < M; ++i)
    {
        int a, b;

        do
        {
            a = rng(0, N - 1)();
            b = rng(0, N - 1)();
        }
        while(a == b or edges.find(pii(a, b)) != edges.end());

        edges.insert(pii(a, b));
        edges.insert(pii(b, a));

        g.add_edge(a, b);
    }

    return g;
}

#endif // GRAPHLIB_H_INCLUDED
