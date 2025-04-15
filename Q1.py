# A palindrome is a word that reads the same backward as forwards, such as madam or racecar. 
# Create a function checkPalindrome to check whether the string passed as its augment is a Palindrome. 
# Do not use any built-in string library function.

def checkPalindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(checkPalindrome("madam"))   
print(checkPalindrome("racecar")) 
print(checkPalindrome("hello"))   
print(checkPalindrome(""))        