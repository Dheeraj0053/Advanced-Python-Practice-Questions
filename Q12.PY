class InvalidRollException(Exception):
    pass

def fee(base_fee, roll):
    if len(roll) != 7:
        raise InvalidRollException("Roll number must be 7 characters long.")
    
    dept = roll[:2]
    if dept not in {'DS', 'CS', 'EE', 'ME'}:
        raise InvalidRollException("Invalid department.")
    
    year = roll[2:4]
    if not year.isdigit() or int(year) > 22:
        raise InvalidRollException("Invalid admission year.")
    
    program = roll[4]
    if program not in {'1', '2'}:
        raise InvalidRollException("Invalid program.")
    
    duration = 4 if program == '1' else 2
    current_year = 22  
    admission_year = int(year)
    
    if admission_year > current_year:
        raise InvalidRollException("Admission year cannot be in the future.")
    
    total_years = min(duration, current_year - admission_year + 1)
    if total_years <= 0:
        return 0
    
    total_fee = 0
    current_fee = base_fee
    for _ in range(total_years):
        total_fee += current_fee
        current_fee = int(current_fee * 1.1)  
    
    return total_fee

print(fee(100000, 'CS20143'))  
print(fee(100000, 'DS18243'))  
print(fee(100000, 'EE16243'))  