# The Traveling Salesperson

1. You have a traveling salesperson
2. The salesperson has to go to five cities. 
3. The salesperson wants to hit all five cities while traveling the minimum distance. 
4. The salesperson adds up the total distance and then picks the path with the lowest distance. 
    -- There are 120 permutations with 5 cities so it will take 120 operations to solve the problem for 5 cities. For 6 cities, the operations increase to 720. 
```md

In general, for n items, it will
take n! (n factorial) operations
to compute the result.

```

This is called O(n!) or factorial time. 

If you are dealing with 100+ cities, it is impossible to calculate the answer in time - the Sun will collapse first!

__This is an unsolved problem in Computer Science.__

The best we can do is come up with an approximate solution to the problem. 