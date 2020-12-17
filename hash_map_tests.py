import unittest

from HashMap import HashMap

'''
6 tests:

1. Can create a hashmap
2. Can insert into a hashmap
3. Can delete key from a hashmap
4. Can expand hashmap
5. Can shrink hashmap
6. Can update values in a hashmap 

'''

class HashMapTests(unittest.TestCase):

    def setUp(self):
        self.HashMap = HashMap(8)
    
    def tearDown(self):
        self.HashMap = None 

    def test_create_hashmap(self):
        self.assertTrue(self.HashMap.is_empty())
        self.assertEqual(self.HashMap.size, 0)
    
    def test_can_insert_into_hashmap(self):
        # check first if 'False' is returned while trying to access a key that doesn't exist in the hashMap
        self.assertFalse(self.HashMap.has_key("test"))
        # insert key into hashMap
        self.HashMap["test"] = "testing"
        # now check if 'True' is returned 
        self.assertTrue(self.HashMap.has_key("test"))
        self.assertTrue(self.HashMap.size, 1)
        self.assertEqual("testing", self.HashMap["test"])

    def test_can_delete_key(self):
        self.HashMap["test"] = "testing"
        # delete the key
        del(self.HashMap["test"])
        # check if has_key returns False 
        self.assertFalse(self.HashMap.has_key("test"))
        self.assertIsNone(self.HashMap["test"])


    def test_hash_map_can_expand(self):
        # initial hashmap bucket size = 8 
        self.assertEqual(8, self.HashMap.num_buckets)
        # populate the hashmap
        count = 1
        while (count <= 9):
            self.HashMap[count] = count
            count += 1
        # check to see if the hashmap has expanded (doubled)
        self.assertEqual(16, self.HashMap.num_buckets)

    def test_hash_map_can_shrink(self):
        self.assertEqual(8, self.HashMap.num_buckets )
        count = 0
        # populate the hashmap
        while (count < 9):
            self.HashMap[count] = count
            count += 1
        # now start deleting 
        while (count > 0):
            del(self.HashMap[count-1])
            count -= 1
        # check to see if hashmap has shrunk 
        self.assertEqual(8, self.HashMap.num_buckets)

    def test_hash_map_can_update(self):
        self.HashMap["test"] = "testing"
        # update test 
        self.HashMap["test"] = "new testing"
        # check
        self.assertEqual("new testing", self.HashMap["test"])

if __name__=='__main__':
    unittest.main()