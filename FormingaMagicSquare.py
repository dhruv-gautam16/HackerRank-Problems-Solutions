s = []
for i in range(3):
    s.append([int(i) for i in input().split()])
orig = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
all_squares = [orig]
all_squares.append(orig[::-1])
all_squares.append([i[::-1] for i in orig])
all_squares.append(all_squares[2][::-1])
all_squares.append([[4, 3, 8], [9, 5, 1], [2, 7, 6]])
all_squares.append(all_squares[4][::-1])
all_squares.append([i[::-1] for i in all_squares[4]])
all_squares.append(all_squares[6][::-1])

#for i in all_squares:
#    for j in i:
#        print(j)
#    print("\n")

least = 99
for i in all_squares:
    temp = 0
    for j in range(3):
        for k in range(3):
            temp += abs(s[j][k]-i[j][k])
    if temp < least:
        least = temp

print(least)