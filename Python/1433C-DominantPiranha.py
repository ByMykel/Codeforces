import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n = ini()
    a = inl()
    if len(set(a)) == 1:
        print(-1)
    else:
        ans = 0
        max_e = max(a)
        for i in range(1, n-1):
            if a[i] != max_e:
                continue
            if a[i] > a[i+1] or a[i] > a[i-1]:
                if a[i] > ans:
                    ans_i = i + 1
                ans = max(ans, a[i])
        if a[0] > ans:
            ans = a[0]
            ans_i = 1
        if a[-1] > ans:
            ans_i = n
        print(ans_i)
