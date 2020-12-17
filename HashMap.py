from LinkedList import LinkedList
import random 

'''
One of the best mapping functions for HashTables is the MAD(Multiply, Add, Divide) compression function. This function has been implemented below.
'''


class HashMap():

    class MADFunction():
        '''
            Essentially, 
            MAD(x) = | ax + b | mod N, where a and b are positive integers chosen at random from a specified range and are not multiples of N.
            This leads to a very small collision rate. 
        '''
        
        def __init__(self, N, p = 40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N


    def __init__(self, num_buckets = 10):
        self.size = 0
        self.num_buckets = num_buckets
        # define linked_lists to handle collisions
        self.table = [LinkedList() for i in range(num_buckets)]
        self.hash_function = HashMap.MADFunction(num_buckets)

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def has_key(self, key):

        ''' 
        returns true if HashMap has the given key, false if it doesn't.
        '''

        index = self.hash_function(key)
        curr_bucket = self.table[index].get_node_with_key(key)
        if curr_bucket:
            return True
        return False 

    def __getitem__(self, key):

        ''' 
        if key is present in hashMap, returns the value, else, raises the KeyError exception. 
        '''

        if (self.has_key(key)):
            index = self.hash_function(key)
            curr_bucket = self.table[index].get_node_with_key(key) 
            return curr_bucket.value

        raise KeyError('That index does not exist in the HashMap.')

    def __setitem__(self, key, value):

        '''
        if the key already exists in the hashMap, updates the key to have the new value.
        else, create a new entry with the given key and value. 
        '''

        index = self.hash_function(key)
        curr_node = self.table[index].get_node_with_key(key)
        if curr_node:
            curr_node.value = value
        else :
            curr_node = self.table[index].add(key, value)
            self.size += 1
            if (self.size > self.num_buckets):
                self.resize()

    def __delitem__(self, key):

        '''
        deletes the item if key exists
        if it doesn't, raises the keyError exception.
        '''

        index = self.hash_function(key)
        curr_node = self.table[index].get_node_with_key(key)
        if curr_node:
            self.table[index].delete(key)
            self.size -= 1
            if (self.size < self.num_buckets / 4):
                self.resize(False)
        else:
            raise KeyError('That index does not exist in the HashMap.')

    def resize(self, grow = True):

        ''' 
        if size of HashMap >= number of buckets, double the number of buckets 
        if size of HashMap < number of buckets / 4, shrink the hashMap by half. 
    
        '''

        num_buckets_new = self.num_buckets * 2 if grow else int(self.num_buckets/2)
        
        # stop at 8 to avoid constant shrinking every time a deletion occurs 
        if num_buckets_new < 8:
            return 

        else:
            self.num_buckets = num_buckets_new

        old_table = self.table 
        self.table = [LinkedList() for i in range(self.num_buckets)]
        self.size = 0 

        # copy data from old table to new table 
        for curr_bucket in old_table:
            curr_node = curr_bucket.header.next
            while curr_node != curr_bucket.trailer:
                index = self.hash_function(curr_node.key)
                self.table[index].add(curr_node.key, curr_node.value)
                self.size += 1
                curr_node = curr_node.next 

        return self 

# a function to print the hash table.
def print_hash_table(ht):
    for i in range(ht.num_buckets):
        print (i, ":", sep = "", end = "")
        curr_bucket = ht.table[i]
        for key in curr_bucket:
            print(key, end = " ")
        print()

hm = HashMap()

