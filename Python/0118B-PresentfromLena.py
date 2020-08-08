#https://codeforces.com/problemset/problem/118/B

n = int(input())
count = 1
space = n*2
k = 1
for i in range(2*n+1):
    numbers = [str(i) for i in range(count)]
    numbers += [str(i) for i in range(count-2, -1, -1)]
    print(space*" " + " ".join(numbers))
    if count == n+1:
        k = -k
    count += k
    space -= k*2
