def equivalent(str1, str2):
    max_len = 0
    result = ''
    
    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substr = str1[i:j]
            for k in range(len(str2) - len(substr) + 1):
                target = str2[k:k+len(substr)]
                if len(substr) != len(target):
                    continue
                if substr in target + target:
                    if len(substr) > max_len or (len(substr) == max_len and substr < result):
                        max_len = len(substr)
                        result = substr
    
    return result if max_len > 0 else ''

print(equivalent('hdj koul', 'pokoudj')) 
print(equivalent('ghajiop', 'abkoidj'))    
print(equivalent('hdj koul', 'pikpiaa'))   