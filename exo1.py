nbr_test = int(input())

for i in range(nbr_test):
    result = []
    code = input()
    nbr_word = int(input())
    for x in range(nbr_word):
        word = input()
        trad_word = ""
        for l in word:
            trad_word += code[(ord(l) - 65) * 2]
        result.append(trad_word)
    doublon = False
    for y in range(len(result)):
        for w in range(y+1, len(result)):
            if result[y] == result[w]:
                doublon = True
                break
        if doublon:
            break
    if doublon:
        print("Case #", str(i + 1), ": YES", sep="")
    else:
        print("Case #", str(i + 1), ": NO", sep="")
            