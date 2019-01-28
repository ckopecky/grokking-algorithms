3.1

Given this:

```md
______________

greet2("Maggie") 
______________

greet("Maggie") 
______________

```

what can you say about the call stack? 

-- I can say that we have a base function called greet(name) - and in the process of calling that function, we came across another function inside that function called greet2(name) which was added to the top of the stack. It has not yet been executed all the way because it has not yet been popped off the stack. 


```py

def increment(num):
    if x == 10:
        print("All Done!")
    else:
        print(num)
        increment(num - 1)



```

3.2

Suppose you accidentally write a recursive function that runs forever. What happens to the stack when your recursive function runs forever. 

-- You will have an infinite loop until max call stack size is exceeded. And then your terminal will abort the process -- called a stack overflow error. 