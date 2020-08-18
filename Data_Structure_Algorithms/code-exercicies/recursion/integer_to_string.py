
def toStr(integer, base):
    convertString = "0123456789ABCDEF"
    # Case Base
    if integer < base:
        return convertString[integer]
    else:
        return toStr(integer // base, base) + convertString[integer % base]

print(toStr(10, 2))

def reverse_string(input):
    """
    Return reversed input string
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """
    if len(input) == 0:
        return ""
    else:
        return reverse_string(input[1:]) + input[0]

def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    
    # Termination / Base condition
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]

        # sub_input is input with first and last char removed
        sub_input = input[1:-1]

        # recursive call, if first and last char are identical, else return False
        return (first_char == last_char) and is_palindrome(sub_input)

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    Example 1:

    input = [1, 2, 3]
    output = [1, 2, 4]
    Example 2:

    input = [1, 2, 9]
    output = [1, 3, 0]
        Example 3:

    input = [9, 9, 9]
    output = [1, 0, 0, 0]
    """
    # Base case 
    if arr == [9]:
        return [1, 0]
    
    # A simple case, where we just need to increment the last digit
    if arr[-1] < 9:
        arr[-1] += 1

    # Case when the last digit is 9.
    else:
        '''Recursive call'''
        # We have used arr[:-1], that means all elements of the list except the last one.
        # Example, for original input arr=[1,2,9], we will pass [1,2] in next call.
        arr = add_one(arr[:-1]) + [0]
        
    return arr

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()


# Tower of Hanoi:

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")