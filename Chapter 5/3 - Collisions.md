Collisions occur when a hash function assigns a value to a spot in hash that is already occupied. We have to learn to work around those collisions to be sure that it still works properly. 

Use a linked list and chance that index to a linked list if it is already occupied. 

But what if all your items get assigned to the first spot because that's what your function tells it to do? The performance slows down quite a bit. We don't want this either. 

