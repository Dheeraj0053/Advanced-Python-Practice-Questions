
def firstLetters(s):
    result = []
    new_word = True
    for char in s:
        if char == ' ':
            new_word = True
        elif new_word:
            result.append(char)
            new_word = False
    return ''.join(result)

print(firstLetters('bad is nice'))          
print(firstLetters('hello other world'))   