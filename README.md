# HashMap

Welcome to my implementation of the HashMap!

## Description

This HashMap was implemented by using Linked Lists as buckets, where each linked list node stores a key/value pair in the HashMap. Since a Linked List allows for constant time insertion and deletion, I prefered using it than to using a normal array. In order to determine which bucket a given key belongs to, I have used the MAD compression function to map the given key into an index on the HashMap. Essentially,

<div align = "center"> MAD(x) = | ax + b | mod N</div>
<br />
(where a and b are positive integers chosen from a specified range and are not multiples of N(number of buckets)).
<br />
<br />
Since the number of key/value pairs never exceed the number of buckets, every lookup takes amortized constant time. On average, each bucket will contain one key/value pair (as ensured by our MAD compression function.) Resizing of the buckets happens only occasionally, further ensuring us that on average, insertion, updating, and deletion takes constant time. To be more specific, expansion or shrinking of the number of buckets only happens when either the key/value pairs exceed the number of buckets, or the number of key/value pairs is less than one-fourth of the number of buckets. 

## HashMap Methods 

* `__len__` :
  Returns the length of the hashmap. 
* `is_empty()` :
  Returns `true` if hashmap is empty, `false` if it is not empty.
* `has_key (key)` :
  Returns `true` if hashmap contains a given `key` 
* `get_keys()` :
  Returns a list of all the keys in the HashMap
* `get_values()`:
  Returns a list of all the values in the HashMap
* `__getitem__` :
  Uses the `[]` operator to get a key in the HashMap. If the `key` doesn't exist, raises a KeyError exception.
* `__setitem__` :
  Uses the `[]` operator to set a given key to a given value. If the key already exists, updates the value to the most recent assignment. 
* `__delitem__` :
  Uses the `[]` operator to delete a given key. If the key doesn't exist, raises a KeyError exception.
* `resize()` :
  Resizes the hashmap by updating the number of buckets 
* I have also included a global `print_hash_table(hashTable)` function that prints the hash table in an appropriate format.  

# Getting Started 

* Clone this repo using the following command on your terminal : `git clone https://github.com/sanidhya-sitaula/myhashmap.git`
* Make sure you have python installed! If not, download the latest version from python.org/downloads 
* Run `cd myhashmap`
* **Run `python3 main.py` to see a brief showdown of the HashMap.**
* Run `python3 hash_map_tests.py` to run tests on the HashMap. 

## For quick use in the terminal 

You can use your HashMap in the terminal in the following way:

* Make sure you're in the project folder.
* After installing python, type `python3` to run python in the terminal. 


```
>>> from HashMap import HashMap
>>> hm = HashMap()
>>> hm[1] = 2 
>>> hm[3] = 4
>>> hm.get_keys()
[1, 3]
>>> hm.get_values()
[2, 4]
>>> del hm[1]
>>> hm.get_keys()
[3]
```


### Testing 

I have included six tests to run on the HashMap using Python's standard library testing framework `unittest`. This means that no further installation is required.

The tests are:

* Can create a hashmap
* Can insert into a hashmap
* Can delete key from a hashmap
* Can expand hashmap 
* Can shrink hashmap
* Can update values in a hashmap

To see details about the inputs I am giving to theses tests and to modify those inputs if you want, please check `hash_map_tests.py`. 

Thanks for checking out my implementation!
