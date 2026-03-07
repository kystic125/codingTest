def multiply(arr1, arr2):
    n = len(arr1)
    c = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += arr1[i][k] * arr2[k][j]
            c[i][j] %= 1000

    return c

def power(array, b):
    n = len(array)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    while b > 0:
        if b % 2 == 1:
            result = multiply(result,  array)
        array = multiply(array, array)
        b //= 2

    return result

n, b = map(int, input().split())
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

answer = power(array, b)

for row in answer:
    print(*row)