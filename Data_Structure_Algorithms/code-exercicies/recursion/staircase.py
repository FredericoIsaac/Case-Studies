
def staircase(n):
    """
    param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase    
    **Example:**

    * `n == 1` then `answer = 1`

    * `n == 3` then `answer = 4`<br>
    The output is `4` because there are four ways we can climb the staircase:
        - 1 step +  1 step + 1 step
        - 1 step + 2 steps 
        - 2 steps + 1 step
        - 3 steps
    * `n == 5` then `answer = 13`
    """
    if n <= 0:
        return 1
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)