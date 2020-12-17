# HashMap

Welcome to my implementation of the HashMap!

## Description

This HashMap was implemented by using Linked Lists as buckets, where each linked list node stores a key/value pair in the HashMap. Since a Linked List allows for constant time insertion and deletion, I prefered using it than to use a normal array. In order to determine which bucket a given key belongs to, I have used the MAD compression function to map the given key into an index on the HashMap. 

Since the number of key/value pairs never exceed the number of buckets, every lookup takes amortized constant time. On average, each bucket will contain one key/value pair (as ensured by our MAD compression function.) Resizing of the buckets happens only occasionally, further ensuring us that on average, insertion, updating, and deletion takes constant time. To be more specific, expansion or shrinking of the number of buckets only happens when either the key/value pairs exceed the number of buckets, or the number of key/value pairs is less than one-fourth of the number of buckets. 

## HashMap Methods 

* __len__
* is_empty
* has_key
* __getitem__
* __setitem__
* __delitem__
* resize

