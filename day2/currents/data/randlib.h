#ifndef RANDLIB_H_INCLUDED
#define RANDLIB_H_INCLUDED

#include<cstdlib>
#include<algorithm>
#include<vector>
#include<numeric>

std::vector<int> range(int a, int b)
{
    std::vector<int> v(b - a);
    iota(v.begin(), v.end(), a);
    return v;
}

std::vector<int> random_permutation(int N, std::mt19937 g)
{
    std::vector<int> v = range(0, N);
    shuffle(v.begin(), v.end(), g);
    return v;
}

std::vector<int> inverse_permutation(std::vector<int> v)
{
    std::vector<int> result(v.size());
    for(size_t i = 0; i < v.size(); ++i) result[v[i]] = (int)i;
    return result;
}

// [x_0, x_1, ..., x_n], [p_0, p_1, ..., p_n] => [x_{p_0}, x_{p_1} ..., x_{p_n}]
template<typename T> std::vector<T> permute(const std::vector<T> &data, const std::vector<int> &permutation)
{
    std::vector<T> result;
    for(size_t i = 0; i < permutation.size(); ++i) result.push_back(data[permutation[i]]);
    return result;
}

template<typename T> std::vector<T> pick(const std::vector<int> &indices, const std::vector<T> &data)
{
    return permute(data, indices);
}

class rng
{
 public:
    rng(int a, int b) : a(a), b(b)
    {}

    int operator()() const
    {
        return a + (rand() % (b - a + 1));
    }

 private:
    int a, b;
};

/*
 * This function returns true with probability $\approx p\in[0,1]$
 */
bool prob(double p)
{
    return std::rand() < p + (p * RAND_MAX);
}

#endif // RANDLIB_H_INCLUDED
