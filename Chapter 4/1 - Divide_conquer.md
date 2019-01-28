### Divide and Conquer

Visual Example:

1. Suppose you are a farmer with a plot of land. 
2. You want to divide this land into _square_ plots. You want these plots to be AS BIG AS POSSIBLE.
3. How do you figure out the largest square size you can use for a plot of land? 

__Divide and Conquer__

Divide and conquer strategies are recursive algorithms. 

Two steps:

1. Figure out the base case. Simplest possible case. 
2. Divide or decrease your problem until it becomes the base case. 

Land size == 1680 meters x 640 meters. 

Easiest case would be if one side was a multiple of another side. 

- For instance, if the land size was 50m x 25m you can deduce that two boxes of 25m would be the largest square size. This would be the base case for that particular problem. 

- Going to our original land size of 1680 x 640, 640 does not go into 1680 evenly. It'll go twice...making one side 1280m...leaving 400m x 640 m left to contend with. 

- In this instance we would divide it again. We'll apply the same algorithm. 

- This time we can only fit one box of 400 x 400 into the land left. So now we have 240m x 400m left. 

- Again....240m x 240m box drawn. left with 240m x 160m box.

- Again....160m x 160m box....left with 80m by 160m box.

- Again....160 is a multiple of 80...so we can divide it into two boxes of 80 by 80. This would be our base case. 

__One thing to remember!__

Divide and Conquer is not a simple algorithm. It's a way to approach a problem that does not necessarily have a prescribed method. 
-----------------

Given: array of numbers

Add up all the numbers and return the total. 

Easy to do with a loop, but how would you use recursion??

```py

#python loop version

def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

print(sum([1, 2, 3, 4]))

```

```js
//javascript loop version

const total = (arr) => {
    let sum = 0;
    for(let i = 0; i < arr.length; i++){
        sum += arr[i];
    }
    return sum;
}

```

How to do this with recursion??

```py
# sum recursion in Python

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))


```

```js

//sum recursion in JS

const listSum = (numList) => {
    let sum = numList[0];
    if(numList.length === 1){
        return sum;
    }
    else {
        numList.shift()
        return sum + listSum(numList);
    }
}

listSum([1, 2, 3, 4, 5, 6]);
```
