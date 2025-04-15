class InvalidInputException(Exception):
    pass

def change(s):
    for char in s:
        if char not in ('R', 'G'):
            raise InvalidInputException("Input must consist of only 'R' and 'G'.")
    
    count_R = 0
    count_G = 0
    for char in s:
        if char == 'R':
            count_R += 1
        else:
            count_G += 1
    return min(count_R, count_G)

print(change('R'))       
print(change('RGRGR'))    
print(change('GRG'))      
# print(change('RGB'))    it will  Raise InvalidInputException