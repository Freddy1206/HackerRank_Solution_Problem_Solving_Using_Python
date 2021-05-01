for _ in range(int(input())):
    n, k = map(int, input().split())
    if not k:
        print(*range(1, n + 1))
    elif n % k or (n // k) & 1:
        print(-1)
    else:
        print(*[x - k if ((x - 1) // k) & 1 else x + k for x in range(1, n + 1)])
