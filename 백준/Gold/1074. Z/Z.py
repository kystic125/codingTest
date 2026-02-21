def func(size, r, c):
    result = 0

    while size > 1:
        half = size//2

        if r < half:
            if c < half:
                pass
            else:
                result += half * half
                c -= half
        else:
            if c < half:
                result += half * half * 2
                r -= half
            else:
                result += half * half * 3
                c -= half
                r -= half
        size = half

    return result
                
n, r, c = map(int, input().split())

n = 2**n
print(func(n, r, c))