def generateMatrix(A):
    m = A
    n = A
    T = 0
    B = m - 1
    L = 0
    R = n - 1
    dir = 0
    spiral = [[0 for i in range(A)] for j in range(A)]
    print(spiral)
    count = 1

    while (T <= B) and (L <= R):
        if dir == 0:
            for i in range(L, R + 1):
                spiral[T][i] = count
                count += 1
            T += 1
            dir = (dir + 1) % 4
        elif dir == 1:
            for i in range(T, B + 1):
                spiral[i][R] = count
                count += 1
            R -= 1
            dir = (dir + 1) % 4
        elif dir == 2:
            for i in range(R, L - 1, -1):
                spiral[B][i] = count
                count += 1
            B -= 1
            dir = (dir + 1) % 4
        elif dir == 3:
            for i in range(B, T - 1, -1):
                spiral[i][L] = count
                count += 1
            L += 1
            dir = (dir + 1) % 4

    return spiral


print(generateMatrix(4))
