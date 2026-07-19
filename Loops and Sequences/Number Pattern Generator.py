#Number Pattern Generator

def number_pattern(n):
    
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    
    if n < 1:
        return 'Argument must be an integer greater than 0.'
        
    result_str = ""
    
    for i in range(1, n + 1):
        result_str += str(i) + " "
        
    return result_str.strip()
