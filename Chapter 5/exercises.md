It is important for hash functions to consistently return the same output for the same input. If they don't, you won't be able to find your item after you it in the hash table!

Which of these hash functions are consistent?

5.1.

f(x) = 1
 
 -- returns one for all input. Consistent but not consistently different yet the same enough for keys. 


5.2

f(x) = rand()

-- returns a random number every time. Not consistent. 

5.3

f(x) = next_empty_slot()

-- would be a different index every time.

5.4 

f(x) = len(x)

-- consistent. 