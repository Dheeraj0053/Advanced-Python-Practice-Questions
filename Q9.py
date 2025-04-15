def moveDups(s):
    seen = set()
    first_occurrence = []
    duplicates = []
    for char in s:
        if char not in seen:
            seen.add(char)
            first_occurrence.append(char)
        else:
            duplicates.append(char)
    return ''.join(first_occurrence) + ('_' + ''.join(duplicates) if duplicates else '')

print(moveDups('cartoon'))   
print(moveDups('network'))    
print(moveDups('aabbcc'))    
print(moveDups('cccbbaaa'))  