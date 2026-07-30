monuments = int(input())
matrix = []
flag = 0

if 4 <= monuments <= 1000:
    for i in range(monuments):
        x, y = map(int, input().split())
        matrix.append((x, y))

# Dictionary to store sums of coordinates (midpoint * 2)
midpoints = {}

for i in range(monuments):
    for j in range(i+1, monuments):
        mx = matrix[i][0] + matrix[j][0]
        my = matrix[i][1] + matrix[j][1]

        if (mx, my) in midpoints:
            a, b = midpoints[(mx, my)]
            # Verify that they do not share points
            if len({a, b, i, j}) == 4:
                flag = 1
                break
        else:
            midpoints[(mx, my)] = (i, j)
    if flag == 1:
        break
    
if flag == 1:
    print("YES")
else:
    print("NO")
