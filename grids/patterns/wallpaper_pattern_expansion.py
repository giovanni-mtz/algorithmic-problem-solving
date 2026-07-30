def wallpaperPattern(userPattern, patternA, patternB):
    result = []
    for row in userPattern:
        expandedRows = [[] for _ in range(len(userPattern))]
        for char in row:
            pattern = patternA if char == "#" else patternB
            for i, subrow in enumerate(pattern):
                expandedRows[i].extend(subrow)
        result.extend(expandedRows)
    return result

n, k = map(int, input().split())

if 2 <= n <= 4 and 1 <= k <= 5:
    pattern = []
    for i in range(n):
        row = []
        for j in range(n):
            value = input()
            row.append(value)
    pattern.append(row)

    patterns = {
        "a": pattern,
        "b": [['.', '.'], ['.', '.']]
    }
    
    for i in range(k - 1):
        wallpaper = wallpaperPattern(pattern, patterns["a"], patterns["b"])
        pattern = wallpaper
        
print(wallpaper)
