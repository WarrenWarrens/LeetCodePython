points =  [[3,1],[1,3],[1,1]]
count = 0
points.sort()

line_count = 0
rect_count = 0
print(points)
for i, p1 in enumerate(points):
    for j, p2 in enumerate(points[i+1:], start=i+1):
        if p1 == p2:
            continue

        # Vertical line (same x)
        if p1[0] == p2[0]:
            x = p1[0]
            y1, y2 = sorted([p1[1], p2[1]])
            has_between = False
            for px, py in points:
                if px == x and y1 < py < y2:
                    has_between = True
                    break
            if not has_between:
                print("Straight vertical:", p1, p2)
                line_count += 1

        # Horizontal line (same y)
        elif p1[1] == p2[1]:
            y = p1[1]
            x1, x2 = sorted([p1[0], p2[0]])
            has_between = False
            for px, py in points:
                if py == y and x1 < px < x2:
                    has_between = True
                    break
            if not has_between:
                print("Straight horizontal:", p1, p2)
                line_count += 1

print("Lines:", line_count, "Rectangles:", rect_count)
