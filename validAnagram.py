
def isAnagram(s, t) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
    



def main():
    s = "hello"
    t = "ooleh"
    answer = isAnagram(s, t)
    print(answer)

if __name__ == "__main__":
    main()