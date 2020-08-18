def deep_reverse(arr):
    """
    Example
    Input: [1, 2, [3, 4, 5], 4, 5]
    Output: [5, 4, [5, 4, 3], 2, 1]
    """
    if len(arr) < 1:
        return arr
    else:
        inverse = deep_reverse(arr[:len(arr)])
        
        output = []
        if type(inverse) is list:
            inverse = deep_reverse(inverse[:len(inverse)])
            output.append(inverse)
        else:    
            output.append(inverse)

