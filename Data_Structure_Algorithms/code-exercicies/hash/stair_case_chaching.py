def staircase(n):
    """
    A child is running up a staircase and can hop either 1 step, 2 steps or 3 steps at a time.
    Given that the staircase has a total n steps,
    write a function to count the number of possible ways in which child can run up the stairs.
    n == 1 then answer = 1
    n == 3 then answer = 4
    The output is 4 because there are four ways we can climb the staircase:
    1 step + 1 step + 1 step
    1 step + 2 steps
    2 steps + 1 step
    3 steps
    """

    num_dict = dict({})
    return staircase_faster(n, num_dict)

def staircase_faster(n, num_dict):
    if n == 1:
            output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output =  staircase_faster(n - 1, num_dict)
        
        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)
            
        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)
        
        output = first_output + second_output + third_output
    
    num_dict[n] = output;
    return output
