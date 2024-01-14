def buy1(n):
    global result
    result += 3 * A[n]


def buy2(n):
    global result
    m = min(A[n:n + 2])
    A[n] -= m
    A[n + 1] -= m
    result += 5 * m


def buy3(n):
    global result
    m = min(A[n:n + 3])
    A[n] -= m
    A[n + 1] -= m
    A[n + 2] -= m
    result += 7 * m


N = int(input())
A = list(map(int,input().split(" "))) + [0, 0]
result = 0
for i in range(len(A) - 2):
    if A[i + 1] > A[i + 2]:
        m = min(A[i], A[i + 1] - A[i + 2])
        A[i] -= m
        A[i + 1] -= m
        result += 5 * m
        buy3(i)
        buy1(i)
    else:
        buy3(i)
        buy2(i)
        buy1(i)
print(result)
