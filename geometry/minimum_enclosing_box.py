import sys

def netFunction(coordinates):
    minX = 10**9
    maxX = -10**9
    minY = 10**9
    maxY = -10**9
    
    for x, y in coordinates:
        if x < minX: minX = x
        if x > maxX: maxX = x
        if y < minY: minY = y
        if y > maxY: maxY = y
    
    width = maxX - minX
    height = maxY - minY
    area = width * height
    return area, width, height

inputData = sys.stdin.read().split()
numInsects = int(inputData[0])
coordinates = [(int(inputData[i]), int(inputData[i+1])) for i in range(1, 2*numInsects, 2)]

print(*netFunction(coordinates))
