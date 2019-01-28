When you write a recursive function, you have to tell it __when__ to stop recursing. 

Every recursive function has two parts: the __base__ case and the __recursive__ case. 

-- Recursive case == function calls itself.

-- Base case == function doesn't call itself again and ends. 

```py

# Python recursion

def countdown(num):
    if num === 0:
        print("Blastoff!")
    else:
        print(num)
        countdown(num-1)

```

```js
//Javascript recursion

const countdown = (num) => {
    if(num === 0) {
        console.log("Blastoff!")
    }
    else {
        console.log(num);
        countdown(num - 1);
    }
}

```