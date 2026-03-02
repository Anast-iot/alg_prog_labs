def min_board_size(N, W, H):
    if W > H:
        lo = W
    else:
        lo = H
    if W > H:
        hi = W * N
    else:
        hi = H * N

    iterations = 0

    while lo < hi:
        iterations += 1
        mid = (lo + hi) // 2
        cols = mid // W
        rows = mid // H
        if cols * rows >= N:
            hi = mid
        else:
            lo = mid + 1

    print(f"Кількість ітерацій: {iterations}")
    return lo

result = min_board_size(5, 1, 4)
if result == 5:
    print("True:", result)
else:
    print("False:", result)

result = min_board_size(2, 1000000000, 999999999)
if result == 1999999998:
    print("True:", result)
else:
    print("False:", result)

print("\nВвести N W H:")
line = input().split()
N, W, H = int(line[0]), int(line[1]), int(line[2])
print(min_board_size(N, W, H))
