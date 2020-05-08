#https://codeforces.com/problemset/problem/937/A

n = int(input())
a = set(map(int, input().split()))
output = len(a) if 0 not in a else len(a)-1
print(output)
