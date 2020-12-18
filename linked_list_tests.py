import unittest
from LinkedList import LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def tearDown(self):
        self.linked_list = None

    def test_initialize(self):
        new_linked_list = LinkedList()
        self.assertTrue(new_linked_list.is_empty())

    def test_add(self):
        self.assertTrue(self.linked_list.is_empty())

        # add a first node that will be both the header and the trailer
        first_node = self.linked_list.add(key=10, value=45)

        self.assertFalse(self.linked_list.is_empty())
        
        self.assertEqual(45, first_node.value)
        self.assertEqual(10, first_node.key)

    def test_get_node_with_key(self):
        
        self.assertIsNone(self.linked_list.get_node_with_key(1))
        self.linked_list.add(key= 10, value = 12)
        self.assertEqual(12, self.linked_list.get_node_with_key(10).value)

    def test_get_node_with_value(self):

        self.assertIsNone(self.linked_list.get_node_with_value(3))
        self.linked_list.add(key = 10, value = 12)
        self.assertEqual(10, self.linked_list.get_node_with_value(12).key)

   

if __name__ == "__main__":
    unittest.main()
