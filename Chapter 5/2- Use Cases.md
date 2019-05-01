## Use Cases

#### Phone Book

* Add a person's name and get the phone number associated with that person

* Enter a person's name and get back the phone number for that person

--- This is a perfect use case for hash tables! Hash tables are great when you want to:

* Create a mapping from one thing to another thing.
* Look something up


```py

phone_book = dict()
phone_book["jenny"] = 8675309
phone_book["emergency"] = 911

print(phone_book["jenny"])

```

```js

const phone_book = {}
phone_book.jenny = 8675309;
phone_book.emergency = 911;

console.log(phone_book.jenny);

```

Mapping a web address to an IP address would be another use case for hash tables. 

#### Preventing Duplicate Entries

Suppose you are running a voting booth. Naturally, every person can vote just once. How do you make sure that they haven't voted before? 

Use a hash!

1. Make a hash to keep track of people who have voted.


2. When someone new comes to vote, check to see if they are already in hash

-- the get function returns the value if the argument is in the hash. Otherwise, it should return `None`. 


```py

voted = {}

def check_voter(name):
    if voted.get(name):
        print("Kick them out!")
    else:
        voted[name] = True        print("Let them vote!")
```

```js

let voted = {};

const checkVoter = (name) => {
    if(voted[name]){
        console.log("Kick them out!");
    } else {
        voted[name] = true;
        console.log("Let them vote!");
    }
}

```

#### Caching

If you work on a website, you may have heard of caching before as a good thing to do. 

Caching allows websites to remember data so that it doesn't have to recalculate a search or something else everytime you look it up. 

```py
server = {'facebook': "http://www.facebook.com/cmvnk1982", 'linkedin': 'https://www.linkedin.com/in/cmvnk'}

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

def get_data_from_server(url):
    print(url)
    if server.get(url):
        return server[url]
    else:
        link = "https://input from user"
        print(link)
        server[url] = link
        return server[url]


```

Recap:

Hashes are good for:

* Modelng relationships from one thing to another thing
* Filtering out duplicates
* Caching/memorizing data instead of making your server do the work. 

