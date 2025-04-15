def subPali(s):
    max_len = 1
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > max_len:
                max_len = len(substr)
    return max_len

print(subPali('bbbabcbabdfb'))  
print(subPali('abcdefg'))      