def shift(s, ccount=0, acount=0):
    if not isinstance(ccount, int) or not isinstance(acount, int) or ccount < 0 or acount < 0:
        raise ValueError("ccount and acount must be non-negative integers.")
    
    def rotate_left(s, n):
        n = n % len(s) if len(s) != 0 else 0
        return s[n:] + s[:n]
    
    def rotate_right(s, n):
        n = n % len(s) if len(s) != 0 else 0
        return s[-n:] + s[:-n]
    
    temp = rotate_left(s, acount)
    result = rotate_right(temp, ccount)
    return result

print(shift('Ninja Hattori'))              
print(shift('Ninja Hattori', acount=3))     
print(shift('Ninja Hattori', ccount=3))     
print(shift('Ninja Hattori', ccount=3, acount=3)) 
print(shift('Ninja Hattori', ccount=3, acount=6))  
print(shift('Ninja Hattori', ccount=6, acount=3)) 