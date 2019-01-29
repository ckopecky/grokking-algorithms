### Hash Functions

A __hash function__ is one where you put in a piece of data and you get back a number, where that piece of data is called a 'string'. 

Hash functions have some requirements:

1. They need to be consistent. For example, suppose you put in 'apple' and get back '4'. Everytime you put in 'apple' you should get back '4'. Without this your hash table will not work. 

2. It should map different words to different numbers. A hash function is no good if it returns '1' for instance for every single word you put in. In the best case, every different word should map to a different number. 

So a hash function maps strings to numbers...what is that good for?

1. Start with an empty array;

2. We'll store all of our prices in this array. 

3. Feed the string 'apple' into our hash function. The hash function spits out '3'. So let's store the price of an apple at index 3 in the array. 

4. Let's add milk. Feeding milk into the hash function outputs 0. Let's store the price of milk at 0. 

5. Keep going and eventually the array will be full of prices. 

6. Now you ask, "What's the price of an avocado?". You don't need to search for it in the array. You just feed "avocado" into the hash function and it will output the index where it is stored at. 

How does this work?

* The hash function consistently maps a name to the same index. Every time you put in "milk", you will get the same number back. So you can use it the first time to find where to store the price of a gallon of milk, and then you can use it to find where you stored the price. 

* The hash function maps different strings to different indices. Everything maps to a different slot in the array where you can store its price. 

* The hash function knows how big your array is and only returns valid indices. So if your array is five items, the hash unction doesn't return 100. That would not be a valid index in the array. 

__Put a hash function and array together and you get a _hash table_!!!__

### Hash Table

Arrays and lists map straight to memory. Hash tables use a function to figure out where to store elements. 

Hash tables == hash maps == dictionaries == associative arrays

You will probably never have to implement hash tables yourself. Python has hash tables...they are called _dictionaries_. In Python you can make a new hash table by using the _dict()_ function. 

```py

book = dict()
#this is an empty hash table.

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print book

# {'avocado': 1.49, 'apple': 0.67, 'milk': 1.49}

print book["avocado"]
#1.49
```

A hash table has keys and values. In the `book` hash, the names of produce are the keys and the prices are the values. A hash table maps those keys to values. 