Give the run time for each of these scenarios in terms of Big O:

1) You have a name, and you want to find the person's phone number in a phone book. 
-- Answer: You would do a binary search since the run time of this would be faster than a simple search. The runtime is O(log n).

2) You have a phone number and you want to find the person's name in the phone book. 
-- Answer: Since you have to search through the whole phone book to find the number associated with the person, you would have to do a simple search. Runtime would be O(n).

3) You want to read the numbers of every person in the phone book. 
Runtime would grow linearly as input grows. Runtime is O(n);

4) You want to read the numbers of just the As. 

Runtime is technically O(n)/26, but we ignore coefficients and just focus on the operation itself. So, runtime would just be O(n).

