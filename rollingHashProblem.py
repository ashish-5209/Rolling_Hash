# Here the problem is to count the number of times the pattern weight is present in the string.
# This problem is called rolling Hash.

def rollinhHash(s, p):

    h1 = 0
    h2 = 0
    count = 0
    for i in p:
        h1 += (ord(i) - ord('a')) + 1

    for i in range(len(p)):
        h2 += (ord(s[i]) - ord('a')) + 1

    if h1 == h2:
        count += 1

    for i in range(len(p), len(s)):
        h2 += (ord(s[i]) - ord('a')) + 1 - ((ord(s[i - len(p)]) - ord('a')) + 1)

        if h1 == h2:
            count += 1

    return count

s = "bacdaabaa"
p = "aab"

print(rollinhHash(s, p))
