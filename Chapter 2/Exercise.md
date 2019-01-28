2.1 

Suppose you are building an app to keep track of your finances:

1. Groceries
2. Movie
3. SFBC Membership

Everyday, you write down everything you spent money on. At the end of the month, you review your expenses, and sum up how much you spent. So, you have lots of inserts and a few reads. Should you use an array or a list? 

-- My guesstimate would be to use a list - especially if you are doing more insertions than reads. It would be faster. 

2.2

Suppose you're building an app for restaurants to take customer orders. Your app needs to store a list of orders. Servers keep adding orders to this list and chefs take orders off the list and make them. It's an order queue: servers add orders to the back of the queue and the chef takes the first order off the queue and cooks it. 

Would you use an array or a linked list to implement this queue? 

-- I would use a linked list since insertions (adding an order) and deletions (cooking an order) are O(1) runtime. This is the difference between linked list and an array - an array would be O(n) runtime on both insertions and deletions. 

2.3 

Let's run a thought experiment. Suppose Facebook keeps a list of usernames. When someone tries to log into Facebook, a search is done for the username. If their list is in the list of usernames, they can log in. 

People log in to Facebook pretty often, so there are a lot of searches through this list of usernames. Suppose Facebook uses binary search to search the list. 

Binary search needs random access. You need to be able to get to the middle of the list of usernames instantly. Knowing this, would you implement the  list as a linked list or an array? 

-- if it needs random access, thoughts should be immediately directly to array - since linked list requires sequential access. 

2.4 

People sign up for Facebook pretty often. Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts? In particular, suppose you're using binary search to search for logins. What happens when you add new users to an array? 

-- the downsides of using an array are when you create a new user and insert it into the array where it should go. Insertions take O(n) runtime and so do deletions. 

-- The array has to be sorted in order to use binary search so the new user has to be inserted at the proper spot in the array. 

What about a hybrid of the two?? An array of linked lists? 

[{all A's},{all B's},{all C's}, etc...]

-- it'll be O(1) runtime to read the correct starting letter since an array reads in O(1) time. Then O(1) to insert or delete for a new user since a linked list has O(1) runtime when it comes to deletion and insertion. It'll have O(n) runtime when it comes to reading through the linked list to find the correct user. 

-- Slower for searching, but faster or about the same for everything else. 

