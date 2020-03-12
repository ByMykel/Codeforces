#https://codeforces.com/problemset/problem/785/A

figures = {
    "Tetrahedron" : 4, 
    "Cube" : 6,
    "Octahedron" : 8,
    "Dodecahedron" : 12,
    "Icosahedron" : 20
}
n = int(input())
solution = 0
for i in range(n):
    solution += figures[input()]
print(solution)
