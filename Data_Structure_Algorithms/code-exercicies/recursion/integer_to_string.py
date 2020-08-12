def toStr(integer, base):
    convertString = "0123456789ABCDEF"
    # Case Base
    if integer < base:
        return convertString[integer]
    else:
        return toStr(integer // base, base) + convertString[integer % base]

print(toStr(10, 2))

def reverse_string(string):
    """
    A function that takes a string as a parameter
    and returns a new string that is the reverse of the old string
    """
    if 
