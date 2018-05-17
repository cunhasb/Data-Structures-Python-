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

    def insert(self, new_element, position):
        if position > 1:

            target_position = self.get_position(position - 1)
            new_element.next = target_position.next
            target_position.next = new_element
        else:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None

        while current:
            if current.value == value:
                if not previous:
                    self.head = current.next
                    return True

                else:
                    previous.next = current.next
                    return True
            previous = current
            current = current.next
        return False

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element
        return self

    def delete_first(self):
        if self.head:
            deleted = self.head
            self.head = self.head.next
            deleted.next = None
            return deleted
