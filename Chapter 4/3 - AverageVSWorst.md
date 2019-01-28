The performance of quicksort heavily depends on the pivot you choose. 

* suppose you always choose the first element as the pivot. And you call quicksort with an array that is already sorted...Quicksort doesn't check to see that the array had already been sorted. So it will still try to sort it. In this instance, you will always have one empty sub-array, which leaves the call-stack super large. 

* suppose you choose the middle element as your pivot. The call stack here will be really short because you are essentially dividing the array in half every time! You hit the base case sooner.

-- the first example is the worst case scenario...the second is the best case scenario. In the worst-case, the stack size is O(n). In the best case the stack size is O(log n). 