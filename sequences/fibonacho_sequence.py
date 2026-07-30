a, b, c, d = map(int, input("").split())
fibonacho = 0
week = 0

if 1 <= a and c <= 100 and 1 <= d <= 10e12:
    while c <= d:
        fibonacho = c * a + b
        c = fibonacho
        week += 1
        
    if c == d:
        print(week - 1)
    else:
        print(week)
