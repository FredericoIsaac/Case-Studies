
# Recursive Solution 
"""
Args: myList: list of items to be permuted
Returns: compound list: list of permutation with each permuted item being represented by a list
"""
import copy                                # We will use `deepcopy()` function from the `copy` module

def permute(inputList):
    
    # a compound list
    finalCompoundList = []                  # compoundList to be returned 
    
    # Terminaiton / Base condition
    if len(inputList) == 0:
        finalCompoundList.append([])
        
    else:
        first_element = inputList[0]        # Pick one element to be permuted
        after_first = slice(1, None)        # `after_first` is an object of type 'slice' class
        rest_list = inputList[after_first]  # convert the `slice` object into a list
        
        # Recursive function call
        sub_compoundList = permute(rest_list)
        
        # Iterate through all lists of the compoundList returned from previous call
        for aList in sub_compoundList:
            
            # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1): 
                
                # A normal copy/assignment will change aList[j] element
                bList = copy.deepcopy(aList)  
                
                # A new list with size +1 as compared to aList
                # is created by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)
                
                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(bList)
                
    return finalCompoundList


# Recursive Solution
"""
Param - input string
Return - compound object: list of all permutations of the input string
"""

def permutations(string):
    return return_permutations(string, 0)
    
def return_permutations(string, index):
    # output to be returned 
    output = list()
    
    # Terminaiton / Base condition
    if index >= len(string):
        return [""]
    
    # Recursive function call
    small_output = return_permutations(string, index + 1)
    
    # Pick a character
    current_char = string[index] 
    
    # Iterate over each sub-string available in the list returned from previous call
    for subString in small_output:
        
        # place the current character at different indices of the sub-string
        for index in range(len(small_output[0]) + 1):
            
            # Make use of the sub-string of previous output, to create a new sub-string. 
            new_subString = subString[0: index] + current_char + subString[index:]
            output.append(new_subString)

    return output


def get_characters(num):
    """
    For example, if you press 23, the following combinations are possible:
    ad, ae, af, bd, be, bf, cd, ce, cf 
    """
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""

# Recursive Solution
def keypad(num):
    
    # Base case
    if num <= 1:
        return [""]

    # If `num` is single digit, get the LIST having one element - the associated string
    elif 1 < num <= 9:
        return list(get_characters(num))

    # Otherwise `num` >= 10. Find the unit's (last) digits of `num` 
    last_digit = num % 10
    
    '''Step 1'''
    # Recursive call to the same function with “floor” of the `num//10`
    small_output = keypad(num//10)               # returns a LIST of strings
    
    '''Step 2'''
    # Get the associated string for the `last_digit`
    keypad_string = get_characters(last_digit)   # returns a string
    
    '''Permute the characters of result obtained from Step 1 and Step 2'''
    output = list()

    '''
    The Idea:
    Each character of keypad_string must be appended to the 
    end of each string available in the small_output
    '''
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)
    
    return output                                # returns a LIST of strings
