def sort(colors):
    nbr_colors = len(colors)
    color_to_int = {}
    last_int = 0
    ints = []
    for i in range(nbr_colors):
        color = colors[i]
        if color not in color_to_int:
            last_int += 1
            color_to_int[color] = last_int
        int_color = color_to_int[color]
        if i > 0 and int_color < ints[-1]:
            return "IMPOSSIBLE"
        ints.append(int_color)
    return " ".join(str(color) for color in sorted(color_to_int, key=color_to_int.get))

nbr_test = int(input())

for i in range(1, nbr_test + 1):
    n = int(input())
    colors = list(map(int, input().split()))
    result = sort(colors)
    print("Case #{}: {}".format(i, result))