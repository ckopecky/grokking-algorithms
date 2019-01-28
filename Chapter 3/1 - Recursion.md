### Recursion

Suppose you are digging through a relative's attic and you find a locked suitcase. 

That relative tells you that the key for the suitcase is probably in this other box. 

However, this box contains other boxes in it as well! 

How do you search for the key? 

Approach 1:

-- Make a pile of the boxes to go through.

-- while pile isn't empty, Grab a box, and look through it. 

-- If you find a box, add it to the pile to look through later. 

-- else you find the key, you are done! 

```py
def look_for_key(main_box):
    pile = main_box
    while len(pile):
        box = pile.grab_a_box()
        for item in box:
            if item == box:
                pile.append(item)
            elif item == key:
                print("found key")


```



Approach 2:

-- Look through the box

-- If you find a box, go to first step

-- if you find a key, you are done! 

```py

def look_for_key(box):
    for item in box:
        if item == key:
            print("found key")
        elif item == box:
            look_for_key(box);

```

Both approaches accomplish the same thing, but the second approach is a little more elegant. _Recursion_ is used when it makes a solution a little more clearer