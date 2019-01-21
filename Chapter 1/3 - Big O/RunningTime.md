# Running Time

When we talk about algorithms, often we talk about how efficient it is. We want to choose the highest efficiency algorithm to solve our problem -- whether you are trying to achieve efficiency in time or space. 

_Simple Search_ uses linear time because it eliminates one choice with each run through. 

_Binary Search_ uses logarithmic time because it eliminates choices by eliminating half of our list at any given time until we find the element we are looking for. 

# __Big O notation__

Big O is a special notation that tells you how fast an algorithm runs.

------

Why is this important? 

-- good to know how fast an algorithm runs - it is very rare you will write your own. 

-----

Two algorithims - one is a simple search and runs at 100ms - the other is a binary search and runs at 7ms. How do you decide which to use? The algorithm needs to be not only fast, but accurate. 

    - on the one hand, binary search is faster. 
    - on the other hand, simple search is easier to write and there will be less chance for bugs. 
    - Let's test both!

Let's assume it takes 1ms to test one element and we want to test the accuracy and speed of 100 elements. 

Simple Search:
    100 elements would have to be checked at the very least - so it will take at least 100ms to run a simple search. 

Binary Search:
    100 elements takes 7 steps roughly to find our element - so it roughly takes 7ms to run. 

What if we were to change that number to a billion? What would happen? Running a linear simple search would take HOURS for something with a billion entries. 

Binary search is faster. 

Bottom Line? Run times don't grow at the same rate for these algorithms. 

** It's not enough to know how long it takes for an algorithm to run, you have to know how the running time increases as the list size increases. 

### This is where Big O Notation comes in!

Big O comapres the number of operations in your code to let you know how fast it goes as the input grows. 