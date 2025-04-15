def reduce(s, k):
    if k == 0:
        return s if all(s.count(c) == s.count(s[0]) for c in set(s)) else ''
    
    from collections import defaultdict
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1
    
    counts = sorted(freq.values())
    min_count = min(counts)
    
    for target in range(min_count, 0, -1):
        total_removal = 0
        new_counts = []
        for cnt in counts:
            if cnt >= target:
                removal = cnt - target
                total_removal += removal
                new_counts.append(target)
            else:
                total_removal += cnt
                new_counts.append(0)
        
        if total_removal == k:
            result = []
            for c in s:
                if freq[c] > 0:
                    if new_counts[list(freq.keys()).index(c)] > 0:
                        result.append(c)
                        new_counts[list(freq.keys()).index(c)] -= 1
            return ''.join(result)
    
    return ''

print(reduce('aabbcc', 0))     
print(reduce('aabbbcc', 1))     
print(reduce('aabbbcc', 2))    
print(reduce('aabbbcc', 3))     
print(reduce('aabbbcc', 4))    
print(reduce('aabbbcc', 5))     
print(reduce('aabbbcc', 6))    
print(reduce('aabbbcc', 7))     
print(reduce('aaaabbcc', 4))