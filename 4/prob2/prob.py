from tempfile import tempdir


alphabet = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

print(alphabet.get("a"))
file = open("input.txt")
N = int(file.readline())

for i in range(0, N):
    S = list(file.readline())
    F = list(file.readline())
    for j in range(S):
        min = 0
        for k in range(F):
            temp1 = (
                (alphabet.get(j) - alphabet.get(k)) * 2
                - alphabet.get(j)
                - alphabet.get(k)
            )
            if alphabet.get(j) == alphabet.get(k):
                continue
            elif temp1 < min:
                min = min + (alphabet.get(j) - alphabet.get(k))
