import linked_list
import unittest


class TestGetPosition(unittest.TestCase):
    """
    Test the get_position function from the linkedlist library
    """

    def test_get_position(self):
        """
        print (ll.get_position(3).value)
        Test that the invoking get_position(3) will return the correct value
        """
    # Set up some Elements
        e1 = linked_list.Element(1)
        e2 = linked_list.Element(2)
        e3 = linked_list.Element(3)
        e4 = linked_list.Element(4)

        # Start setting up a LinkedList
        ll = linked_list.LinkedList(e1)
        ll.append(e2)
        ll.append(e3)

    # Test
        result = ll.get_position(3).value
        self.assertEqual(result, 3)

    # Test insert

    def test_insert(self):
        """
        Should insert element into position, should print 4
        """

        # Set up some Elements
        e1 = linked_list.Element(1)
        e2 = linked_list.Element(2)
        e3 = linked_list.Element(3)
        e4 = linked_list.Element(4)

        # Start setting up a LinkedList
        ll = linked_list.LinkedList(e1)
        ll.append(e2)
        ll.append(e3)

        # Test
        ll.insert(e4, 3)
        result = ll.get_position(3).value
        self.assertEqual(result, 4)

    # Test delete

    def test_delete(self):
        """
        Should delete an element from the LinkedList, should print 2
        """

        # Set up some Elements
        e1 = linked_list.Element(1)
        e2 = linked_list.Element(2)
        e3 = linked_list.Element(3)
        e4 = linked_list.Element(4)

        # Start setting up a LinkedList
        ll = linked_list.LinkedList(e1)
        ll.append(e2)
        ll.append(e3)

        # Insert Element
        ll.insert(e4, 3)

        # Delete Element
        ll.delete(1)

        # Test
        result = ll.get_position(1).value
        self.assertEqual(result, 2)
        result = ll.get_position(2).value
        self.assertEqual(result, 4)
        result = ll.get_position(3).value
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
