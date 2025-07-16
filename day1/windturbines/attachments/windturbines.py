N, M, Q = map(int, input().split())

u = [0] * M
v = [0] * M
c = [0] * M
for i in range(M):
    u[i], v[i], c[i] = map(int, input().split())

l = [0] * Q
r = [0] * Q
for i in range(Q):
    l[i], r[i] = map(int, input().split())

ans = [0] * Q

for i in range(Q):
    print(ans[i])
