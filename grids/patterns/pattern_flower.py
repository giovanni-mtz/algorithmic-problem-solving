y, x = map(int, input("").split())
grid = []
location1 = []
location2 = []
location3 = []
location4 = []
    
for i in range(y):
    line = input()
    grid.append(list(line))

if 5 <= x <= 1000 and 2 <= y <= 1000:
    for i in range(y):    
        if "*" in grid[i]:
            if grid[i].count("*") == 1:
                if not location2:
                    location2.append(grid[i].index("*"))
                elif location2 and not location4 and location3:
                    location4.append(grid[i].index("*"))
            else:
                if not location1:
                    location1.append(grid[i].index("*"))
                    location1.append(grid[i].index("*") + grid[i].count("*") - 1)
                elif location1 and not location3:
                    location3.append(grid[i].index("*"))
                    location3.append(grid[i].index("*") + grid[i].count("*") - 1)

    if location4[0] == location3[0]:
        print("Double Petal Flower")  
    else:
        print("Triple Corolla Flower")
