def distChar(s1, s2):
    def get_unique_chars(s):
        unique = []
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
                unique.append(char)
        return unique
    
    unique_s1 = get_unique_chars(s1)
    unique_s2 = get_unique_chars(s2)
    
    uncommon = []
    for char in unique_s1:
        if char not in unique_s2:
            uncommon.append(char)
    for char in unique_s2:
        if char not in unique_s1 and char not in uncommon:
            uncommon.append(char)
    
    if not uncommon:
        return ''
    
    
    for i in range(len(uncommon)):
        for j in range(i + 1, len(uncommon)):
            if uncommon[i] > uncommon[j]:
                uncommon[i], uncommon[j] = uncommon[j], uncommon[i]
    
    return ''.join(uncommon)

print(distChar('characters', 'alphabets'))  
print(distChar('apples', 'oranges'))        
print(distChar('apples', 'apples'))        