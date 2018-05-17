class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head

        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head.next = new_element

    def get_position(self, position):
        current = self.head
        counter = 1

        while counter <= position and current:
            if counter == position:
                return current
            current = current.next
            counter += 1

        return None
