def delVowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = []
    for char in s:
        if char not in vowels:
            result.append(char)
    return ''.join(result)

print(delVowels('SfgEtfjofubjiekp'))  
print(delVowels('aEiou'))             