### Deletions

What if you want to delete an element? 

__Lists__ are better because you just need to change what the previous element points to. With arrays, everything needs to be moved up when you delete an element. 

__Here are the run times for common operations on arrays and linked lists:__


|           | Arrays  |  Linked Lists |
|---        |---      |---            |
| Reading   |  O(1)   | O(n)          |
| Insertion | O(n)    | O(1)          |
| Deletion | O(n)    | O(1)          |


Why have arrays in the first place?

-- Arrays allow for random access. _Random access_ means that you can jump directly to an element. 

-- Linked Lists allow for sequential access. _Sequential access_ means that you have to visit each preceding element unti you get to the one you are looking for. Linked Lists ONLY have sequential access. 

_Arrays are faster at reads, which is why they are used a lot!_
    
    - a lot of use cases require random access reads. 

Arrays and linked lists are used to implement other data structures. 