### Quicksort

Quicksort is, as the name suggests, a sorting algorithm. It's much faster than selection sort, and is frequently used in real life. 

_Quicksort uses Divide and Conquer_

Let's use Quicksort to sort an array....what's the simplest array that a sorting algorithm can handle? 

Some arrays don't need to be sorted at all! 

    - empty arrays
    - arrays with one element

These will be your base case. You can just return those arrays as is. No need to sort anything. 

What about bigger arrays? 
    - An array with just two elements is pretty easy to sort as well. Check if the first element is smaller. If it isn't, swap them. 

-  Three plus-length arrays. You want to break it down to the most basic case. 
    - First, pick an element from the array. We call this the __pivot__. 
    - Next, find the elements smaller than the pivot and larger than the pivot. We call this __partitioning__. 
        * Now we have three sub-arrays:  A sub-array of all the numbers < pivot, the pivot, and a sub-array of all numbers > pivot. 

    - The two sub-arrays are not sorted. They are just partitioned. But if they were sorted, then sorting the whole array would be easy. It would be `sorted array` = `left array` + `pivot` + `right array`. 
    
    - How do you sort the sub-arrays? 
    * The quicksort base case already knows how to sort arrays of two elements and empty arrays. So if you call quicksort on the two sub-arrays and then combine the results, you get the sorted array!
    