def RemoveRepeat(s):
    for i in range(0, len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                s = s.replace(s[i], "")
    return s