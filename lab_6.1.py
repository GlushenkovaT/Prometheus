
def count_holes(n):
    number = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 1, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1}
    counter = 0
    
    if isinstance(n, (int, str)):
        n = str(n)
    
        try:
            if not n.isdigit():
                n = str(abs(int(n)))
        except ValueError:
            return "ERROR"
 
        for j in str(abs(int(n))):
            if j in number:
                counter += number[j]
    
        return counter
    
    else:
        return "ERROR"