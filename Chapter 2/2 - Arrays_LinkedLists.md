# Arrays and Linked Lists

Sometimes you need to store a list of elements in memory. Suppose you're writing an app to manage your todos. You'll want to store those todos as a list in memory. 

__Array or Linked List?__

Array:

* using an array means that all of your todos are stored contiguously (right next to each other) in memory. 
    - Suppose, though, that you want to add to that array? But the next slot in memory is taken up by something else? What will you do? 
    - Your computer will have to find a different spot in memory where it can fit the new size of the array. Then you need to move all of your tasks there. 
    - Adding items to an array can be a big pain for your computer. If you need to move your array to a new spot every time it grows, adding a new item will be really slow. 

    You can "save" the allotted amount if you know how large your array will be. However, if you need to increase the size of the array for whatever reason, you're back to moving the whole array to a new space in memory. So, while a good workaround, it is not the perfect solution. 

    __Linked Lists__ solve this problem. 

    ## Linked Lists

    With linked lists your items can be stored anywhere in memory. Each item stores the address of the next item in the list. 

    With linked lists, you never have to move your items...

    _Then what are arrays good for?_ 

    You are not able to go directly to a particular index in an a linked list...you have to start at the beginning of the linked list to get to the address of the item you are wanting. Linked lists are great if you are going to look at all of your items in a list at once...but not if you need to look at something individually. 

    Runtime for insertion and reading on linked lists and arrays:

|           | Arrays  |  Linked Lists |
|---        |---      |---            |
| Reading   |  O(1)   | O(n)          |
| Insertion | O(n)    | O(1)          |

