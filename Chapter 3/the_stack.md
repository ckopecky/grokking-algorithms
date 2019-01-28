### The call stack

Need to know what the stack is first:
__STACK__

* new item (first out)
* item (next out)
* item (...)
* item (...)
* first item (last out)

-- the stack adopts a first in, last out (FILO) philosophy. 

-- two actions: push(insert) and pop (delete and read)


-- Your computer uses  a stack internally called the _call stack_. 

Let's walk through what happens when you call a function. 

```py

def greet(name):
    print("hello," + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye!")

```

1. When you invoke a function, your computer allocates a box for that function call. Suppose you call `greet("Maggie)`
2. Let's use the memory. The variable `name` is set to `Maggie`. That needs to be saved in memory.

```md

______________

greet("Maggie") <--first element in stack.
______________

```

3. According to the function, your terminal will print `"Hello, Maggie!"` to stdout. Then comes the call for `greet2("Maggie")`.

4. Your computer then allocates another box for that function call (the greet2 function call). It gets added to the top of the stack.


```md
______________

greet2("Maggie") <-- next element goes on top of stack. 
______________

greet("Maggie") <--first element in stack.
______________

```

5. When you return back to the original function after the function call to greet2(name), greet2(name is popped off)...so we are back to:

```md

______________

greet("Maggie") <--first element in stack.
______________

```

...and then we pick up where we left off in the function. Then we print("getting ready to say bye") before calling the bye() function. 


```md
______________

bye() <-- next element goes on top of stack. 
______________

greet("Maggie") <--first element in stack.
______________

```

When bye() is through, it is then popped off the stack. Then you're just left with the greet function again. When there is nothing left to do in the greet function, it too is popped off the stack and you're done! 


