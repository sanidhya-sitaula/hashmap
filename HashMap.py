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


    def __init__(self, num_buckets = 64):
        self.size = 0
        self.num_buckets = num_buckets
        # define linked_lists to handle collisions
        self.table = [LinkedList() for i in range(num_buckets)]
        self.hash_function = HashMap.MADFunction(num_buckets)

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def __getitem__(self, key):
        index = self.hash_function(key)
        curr_bucket = self.table[index].get_node_with_key(key) 
        return curr_bucket.value

    def __setitem__(self, key, value):
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
        index = self.hash_function(key)
        curr_node = self.table[index].get_node_with_key(key)
        self.table[index].delete(key)
        self.size -= 1
    
    def print_table(self):
        for i in range(self.num_buckets):
            print(i, ": ", sep="", end="")
            curr_bucket = self.table[i]
            for key in curr_bucket:
                print(key, sep="", end=" ")
            print()


hm = HashMap()

for i in range(0, 10):
    hm[i] = i + 3

hm.print_table()
