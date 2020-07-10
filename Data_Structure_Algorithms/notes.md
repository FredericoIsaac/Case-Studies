# Udacity Course - Data Structure & Algorithms

## Introduction

### How to Solve Problems:

#### The Problem:

Given your birthday and the current date, calculate your age in days. Compensate for leap years. Assume that the birthday and current date are correct dates (no time travel). Simply put, if you were born 1 Jan 2012 and today's date is 2 Jan 2012 you are 1 day old.

* Dont Panic

* Possible inputs? What are the inputs?
    * Given your birthday and the current date, calculate your age in days.
    * Inputs : two dates
        * Checks inputs: 
            * Second date must not be before first date

* What are the outputs?
    * Return a number giving the number of days between the first date and the second date

* Solving the problem
    * Work out examples - understand the relationship
        * Create examples, for each give the expected output or undefined if there is no defined output.
            * daysBetweenDates(2012, 12, 7, 2012, 12, 7)  -> 0
            * daysBetweenDates(2012, 12, 7, 2012, 12, 8)  -> 1
            * daysBetweenDates(2012, 12, 8, 2012, 12, 7)  -> undefined
            * daysBetweenDates(2012, 6, 29, 2013, 6, 29)  -> 365
            * daysBetweenDates(2012, 6, 29, 2013, 6, 31)  -> undefined
        
        * Resolve examples by hand first
            * daysBetweenDates(2013,1,24,2013,6,29)

                    Jan 24 - Jan 31 = 7
                    + Feb            28
                    + March          31
                    + April          30
                    + May            31
                    + Jun 1 - 29     29
                    Total            156
        
        * Simple mechanical solution - simplify the solution
            * Pseudocode:

                    days = 0
                    while date1 is before date2:
                        date1 = day after date1
                        days += 1
                    return days
            
            * Break the problem in small peaces, and start by the order that you think is best.
            
                * First lets try to code nextDay(year, month,day)

                        def nextDay(year, month, day):
                            """ Warning: this version incorrectly
                            assumes all months have 30 days!"""
                            if day < 30:
                                return year, month, day + 1
                            else:
                                if month < 12:
                                    return year, month + 1, 1
                                else:
                                    return year + 1, 1, 1 
            
            * Test every peace of the code, to know your are in the right track
                * Example of tests:

                        def test():
                            # tests with 30-day months!
                            assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
                            assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
                            assert nextDay(2013, 1, 1) == (2013, 1, 2)
                            assert nextDay(2013, 4, 30) == (2013, 5, 1)
                            assert nextDay(2012, 12, 31) == (2013, 1, 1)
                            print "Tests finished."

Summary

1. What are the inputs
2. What are the outputs
3. Work through some examples by hand
4. Simple mechanical solution
5. Develop incrementally and test as we go

## Efficiency

Let's look again at this function from above:

    def say_hello(n):
        for i in range(n):
            print("Hello!")

As the input increases, the number of lines executed also increases.

But we can go further than that! We can also say that as the input increases, the number of lines executed increases by a proportional amount. Increasing the input by 1 will cause 1 more line to get run. Increasing the input by 10 will cause 10 more lines to get run. Any change in the input is tied to a consistent, proportional change in the number of lines executed. This type of relationship is called a **linear relationship**.

Now here's a slightly modified version of the say_hello function:

    def say_hello(n):
        for i in range(n):
            for i in range(n):
                print("Hello!")

Notice that when the input goes up by a certain amount, the number of operations goes up by the square of that amount. If the input is 2, the number of operations is 2^2. If the input is 3,the number of operations is 3^2 or 9.

To state this in general terms, if we have an input, n, then the number of operations will be n^2. This is what we would call a quadratic rate of increase.

We will use this graph as a referece and reminder of the importance of the run time of an algorithm. We have the number of inputs (n) on the X axis and the the number of operations required (N) on the Y axis.

![algorithms-rate](/Data_Structure_Algorithms\images\algoritgms-rate.png)

Notice that if n is very small, it doesn't really matter which function we use—but as we put in larger values for n, the function with the nested loop will quickly become far less efficient.

### Order

We should note that when people refer to the rate of increase of an algorithm, they will sometimes instead use the term order. Or to put that another way:

The rate of increase of an algorithm is also referred to as the order of the algorithm.

### Big O Notation
[Video explanation of how to get the big O of O(n)](https://www.youtube.com/watch?v=QF4hPt1WHog)

When describing the efficiency of an algorithm, we could say something like "the run-time of the algorithm increases linearly with the input size". This can get wordy and it also lacks precision. So as an alternative, mathematicians developed a form of notation called big O notation. The "O" in the name refers to the order of the function or algorithm in question.

O(n):

    def say_hello(n):
        for i in range(n):
            print("Hello!")


O(n^2):

    def say_hello(n):
        for i in range(n):
            for i in range(n):
                print("Hello!")

 We've been approximating efficiency by counting the number of lines of code that get executed. But when we are thinking about the run-time of a program, what we really care about is how fast the computer's processor is, and how many operations we're asking the processor to perform. Different lines of code may demand very different numbers of operations from the computer's processor. For now, counting lines will work OK as an approximation, but as we go through the course you'll see that there's a lot more going on under the surface.

 In n^2 + 5n, the 5 has very little impact on the total efficiency—especially as the input size gets larger and larger. Asking the computer to do 10,005 operations vs. 10,000 operations makes little difference. Thus, it is the n^2 that we really care about the most, and the +5 makes little difference.

![big-O - https://www.bigocheatsheet.com/](/Data_Structure_Algorithms\images\big-O.png)


#### Quadratic Example

```python
# O(n^2)

def Quad_Example(our_list):
    for first_loop_item in our_list:
        for second_loop_item in our_list:
            print ("Items: {}, {}".format(first_loop_item,second_loop_item))
            
            
Quad_Example([1,2,3,4])

%time
```

    Items: 1, 1
    Items: 1, 2
    Items: 1, 3
    Items: 1, 4
    Items: 2, 1
    Items: 2, 2
    Items: 2, 3
    Items: 2, 4
    Items: 3, 1
    Items: 3, 2
    Items: 3, 3
    Items: 3, 4
    Items: 4, 1
    Items: 4, 2
    Items: 4, 3
    Items: 4, 4
    CPU times: user 3 µs, sys: 0 ns, total: 3 µs
    Wall time: 6.2 µs


#### Log Linear Example 


```python
# O(nlogn)

# Don't worry about how this algorithm works, we will cover it later in the course!

def Log_Linear_Example(our_list):
    
    if len(our_list) < 2:
        return our_list
    
    else:
        mid = len(our_list)//2
        left = our_list[:mid]
        right = our_list[mid:]

        Log_Linear_Example(left)
        Log_Linear_Example(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                our_list[k]=left[i]
                i+=1
            else:
                our_list[k]=right[j]
                j+=1
            k+=1

        while i < len(left):
            our_list[k]=left[i]
            i+=1
            k+=1

        while j < len(right):
            our_list[k]=right[j]
            j+=1
            k+=1
        
        return our_list

Log_Linear_Example([56,23,11,90,65,4,35,65,84,12,4,0])

%time
```

#### Linear Example


```python
# O(n)

def Linear_Example(our_list):
    for item in our_list:
        print ("Item: {}".format(item))

Linear_Example([1,2,3,4])

%time
```

#### Logarithmic Example


```python
# O(logn)

def Logarithmic_Example(number):
    if number == 0: 
        return 0
    
    elif number == 1: 
        return 1
    
    else: 
        return Logarithmic_Example(number-1)+Logarithmic_Example(number-2)

    
Logarithmic_Example(29)

%time
```

#### Constant Example


```python
# O(1)

def Constant_Example(our_list):
    return our_list.pop()

Constant_Example([1,2,3,4])

%time
```


### Space Complexity Examples

When we refer to space complexity, we are talking about how efficient our algorithm is in terms of memory usage. This comes down to the datatypes of the variables we are using and their allocated space requirements. In Python, it's less clear how to do this due to the underlying data structures using more memory for house keeping functions (as the language is actually written in C).

For example of the learning experience: 

|Type |	Storage size|
| -----|-----|
|char |	1 byte|
|bool |	1 byte|
|int |	4 bytes|
|float |	4 bytes|
|double |	8 bytes|


Example 1

    def our_constant_function():

        x = 3 # Type int
        y = 345 # Type int
        z = 11 # Type int

        answer = x+y+z

        return answer

So in this example we have four integers (x, y, z and answer) and therefore our space complexity will be 4*4 = 16 bytes. This is an example of constant space complexity, since the amount of space used does not change with input size.

Example 2

    def our_linear_function(n):

        n = n # Type int
        counter = 0 # Type int
        list_ = [] # Assume that the list is empty (i.e., ignore the fact that there is actually meta data stored with Python lists)

        while counter < n:
            list_.append(counter)
            counter = counter + 1

        return list_

So in this example we have two integers (n and counter) and an expanding list, and therefore our space complexity will be 4*n + 8 since we have an expanding integer list and two integer data types. This is an example of linear space complexity.


