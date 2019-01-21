# Binary Search

__Binary Search__ is an algorithm that takes an input of sorted elements. If an element you are looking for is in that list, it will return the position of that element. Otherwise, binary search will return <code>null</code>.

__Simple Search__ occurs when you eliminate one element with each guess. Worst-case scenario is that it would take the length of the number of elements to guess what you're looking for! There's a better way to do this. 

To make this faster, we use binary search. This occurs when we select the element right in the middle, determine if it's too much, too little or just right. In two of those cases, we eliminate half the elements. 

We choose the element in the middle every time, thus eliminating another half of what is left, until we get to the element that we are looking for. 



Example: 
```md
Q: Say we were looking for a word in the dictionary. If the dictionary had 240,000 words, how many would it steps could it potentially take to find the word you are looking for? 

A: It could potentially take up to 240,000 steps! 

Q: How would this differ if we were using binary search? 

A: 
    240,000/2 = 120,000
    120,000/2 = 60,000
    60,000/2 = 30,000
    30,000/2 = 15,000
    15,000/2 = 7,500
    7,500/2 = 3,750
    3,750/2 = 1,875
    1,875/2 = 938 (rounded)
    938/2 = 469
    469/2 = 235 (rounded)
    235/2 = 118 (rounded)
    118/2 = 59
    59/2 = 30
    30/2 = 15
    15/2 = 8
    8/2 = 4
    4/2 = 2
    2/2 = 1

    Worst case scenario would only be 18 steps! 

```

__Binary search will take _log base 2 n steps_ to run in the worst case, whereas simple search will take n steps__

## Uhhhhhh....remind me what logs are again? 

__Logarithms__ (log base n of x)

It's like asking " How many n's do we multiply together to get x? 

Logs are the _flip_ of exponentials. 

When we talk about log in terms of Big O notation, we are always talking about log base 2. 