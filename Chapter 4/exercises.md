4.1

Write the code for the earlier sum function

```py

def sumNoRecursion(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


def sumRecursion(arr):
    sum = arr[0]
    if len(arr) == 1:
        return sum

    else:
        return sum + sumRecursion(arr[1:])

```

```js

const totalNoRecursion = (arr) => {
    let sum = 0;
    for(let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

const totalRecursion = (arr) => {
    let sum = arr[0];
    if(arr.length === 1) {
        return sum;
    }
    else {
        arr.shift();
        return sum + totalRecursion(arr);
    }
}


```

4.2

Write a recursive function to count the number of items in a list.

```py

def recursiveCount(arr):
    count = 1
    if len(arr) == 1:
        return count
    else:
        return count + recursiveCount(arr[1:])
    return None

```

```js

const recursiveCount = (arr) => {
    let count = 1;
    if(!arr.length){
      return 0;
    }
    if(arr.length === 1){
        return count;
    }
    else {
        arr.shift()
        return count + recursiveCount(arr);
    }
}
```

4.3 

Find the max number in a list.

```py

#Python

def maximumNoRecursion(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

def maxWithRecursion(arr):
  if len(arr) == 1:
    return arr[0]
  else:
    max = maxWithRecursion(arr[1:])
    if arr[0] > max:
      return arr[0]
    else:
      return max

print(maxWithRecursion([6, 89, 333, 2, 78]))
```

```js
//JS version

const maxWithRec = (arr) => {
    if (arr.length === 1) {  // Step1: set up your base case
        return arr[0];
    } else {  
    console.log(arr)
        return Math.max(arr.shift(), maxWithRec(arr)); // Step2: rec case
    }
}

console.log(maxWithRec([33, 22, 34, 44, 11, 0, 634]));

```

4.4

Remember binary search from chapter 1? It's a divide and conquer algorithm too. Can you come up with a base case and recursive case for binary search too? 

```py

def binarySearchRecursion(arr, number):
    print(number)
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        if arr[0] == number:
            print("found")
            return arr[0]
        else:
            print("not found")
            return None
    else :
        mid = round(len(arr)/2);
        print(arr[mid], "mid")
        print(number, "number")
        if arr[mid] is number:
            print(number, "number mid")
            print(arr[mid], "I found it")
            return arr[mid]
        elif arr[mid] > number:
            print("mid >")
            print(arr[:mid], "arr[:mid")
            return binarySearchRecursion(arr[:mid], number)
        else:
            print("mid <")
            print(arr[mid:], "arr[mid:]")
            return binarySearchRecursion(arr[mid:], number)
    return None
    
print(binarySearchRecursion([2, 3, 14, 18, 55, 66],33))
```
```js

const binarySearchRecursion = (arr, number) => {
    if(arr.length === 0) {
        return null;
    }
    else if(arr.length === 1) {
        if(arr[0] === number){
            console.log("found");
            return arr[0];
        }
        else {
            console.log("not found")
            return null;
        }
    }
    else {
        let mid = Math.round(arr.length/2);
        if(arr[mid] === number){
            console.log("I found it");
            return arr[mid];
        }
        else if(arr[mid] > number){
            console.log("mid > number");
            return binarySearchRecursion(arr.slice(0, mid), number);

        }
        else {
            console.log("mid < number");
            return binarySearchRecursion(arr.slice(mid), number);
        }
    }

}


    
console.log(binarySearchRecursion([2, 3, 14, 18, 55, 66],33))


```

How long do each of these operations take?


4.5

Printing the value of each element in an array.

-- O(n)

Doubling the value of each element in an array

-- O(n)

Doubling the value of just the first element in the array.

-- O(1)

Creating a multiplication table with all the elements in an array. So if your array is [2, 3, 7, 8, 10], you first multiple every element by 2, then every element by 3, then by 7 and so on. 

-- we have each element is being touched twice... O(n) stack * O(n) items...so O(nˆ2)




