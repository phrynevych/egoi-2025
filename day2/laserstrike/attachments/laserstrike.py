P, N = map(int, input().split())

if P == 1:
    a = [0] * (N - 1)
    b = [0] * (N - 1)
    for i in range(N - 1):
        a[i], b[i] = map(int, input().split())

    message = "0101"
    l = [0] * (N - 1)

    print(message)
    for i in range(N - 1):
        print(l[i])
else:
    message = input()

    for i in range(N - 1):
        a, b = map(int, input().split())

        guess_a = True

        if guess_a:
            print(a)
        else:
            print(b)
