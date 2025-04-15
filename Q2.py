# Create a function minIndexFirstString that takes two strings strl and str2 as arguments and finds the largest index of a character in strl that is also present in str2. If the strings have no characters in common, return -1. Do not use any built-in string library function.
#minIndexFirstString('tiger', 'integer') -> 4
#minIndexFirstString('integer', 'tiger') -> 6

def minIndexFirstString(str1, str2):
    max_index = -1
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                if i > max_index:
                    max_index = i
                break
    return max_index
print(minIndexFirstString('tiger', 'integer'))  
print(minIndexFirstString('integer', 'tiger'))  
print(minIndexFirstString('abc', 'def'))        