def solve_case(i, settings, light):
    street = [False] * settings[0]
    for x in range(settings[2]):
        emplacement_min = light[x] - settings[1]
        if emplacement_min < 0:
            emplacement_min = 0
        emplacement_max = light[x] + settings[1]
        if emplacement_max > settings[0]:
            emplacement_max = settings[0]
        emplacements = (j for j in range(emplacement_min, emplacement_max))
        for j in emplacements:
            street[j] = True
        if all(street):
            print("Case #", str(i + 1), ": ", str(x + 1), sep="")
            return
    print("Case #", str(i + 1), ": IMPOSSIBLE", sep="")

nbr_test = int(input())

for i in range(nbr_test):
    settings = [int(x) for x in input().split()]
    light = [int(x) for x in input().split()]
    solve_case(i, settings, light)