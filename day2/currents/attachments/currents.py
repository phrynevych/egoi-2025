N, M = map(int, input().split())

a = [0] * M
b = [0] * M
for i in range(M):
    a[i], b[i] = map(int, input().split())

ans = [0] * (N - 1)

print(*ans)
