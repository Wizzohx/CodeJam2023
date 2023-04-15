nbr_test = int(input())

for i in range(nbr_test):
    x = int(input()) - 1
    print(x)
    print(x % 26)
    letter = chr((x % 26) + 65)
    print(letter)
    print("Case #", str(i + 1), ": ", letter, sep="")