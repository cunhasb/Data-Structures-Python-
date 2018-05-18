# Data-Structures-Python-
Data Structures Python - Linked Lists

Original Post
https://medium.com/p/2603803e9139

This is post is, or better yet , will be part of a series of other posts related to Data Structures in Computer Science.
Data Structures and Collections
So let's start from the beginning and first define what's a data Structure, Data Structure in Computer Science is just a way of storing information (data) in a computer for later access and manipulations. You can think of them as a collection or group of related structures that should be accessed and manipulated as a group, so the information that they contain must provide ways for the computer to find, insert, and delete information. The implementation of data structures is dependent on the language used, and varies considerably from language to language, its beyond the scope of this blog to compared them. What I'll try to convey is just a high-level definition and its uses independent of the language used.

Pet Collection that contains a Cat CollectionCollections on its own can't do much in Programming, because even tough they can group things (data, zero, other collections), they are inherently without order. So even a seemingly easy task of "give me the 4th cat in my collection" would prove to be impossible, since we don't know where the collection starts, ends or anything else for that matter. So what then?

Lists to the Rescue…
Lists usually have all the properties of a collection but with some extra superpowers, and the most important is Order.
A list represents a countable number of order values, or a finite sequence. They representation depends largely on the language and is often defined using commas, semicolons, spaces within a pair of parentheses(), brackets[], curly braces{} or angle brackets<>.

> > > [('Bruce','Wayne'),('Peter','Parker'),('Tony','Stark')]['banana','orange','apple','pear','kiwi']
> > > {'a','b','c','d','e','f'}
> > > Linked-Lists
> > > Linked lists are extensions of collections, thus are used to group things, and since they are lists they must have some sort of order, but unlike arrays(which we are not going to cover here) that have indexes, Linked list have a reference or pointer the tells it what element comes after it, and sometimes before it or even both, like in the case of Doubly-Linked-Lists.
> > > Singly-Linked-ListsIn the picture above we have a Singly-Linked-List with 3 elements, each element is only concerned with two things, it's own data, and the next element in the chain. The first element in this case 5 is called the head and it does not know anything about the element 7, but it knows about element 55 which knows about 7 and since 7 does not have any next element, it means that we are at the end of the list, or at its tail.
> > > A good analogy to linked lists would be a simple webpage, that contains all the search results for cats, we won't be able to list all the results in one page, so we are giving one page full of results and a "Next" button to go to the next page, the head. We will be hitting that "Next" button until that button no longer is displayed, meaning that we are at the end of the list, its tail.
> > > Linked Lists in memory blocsAssuming that the above picture are memory addresses, we can see how linked lists are saved in memory. In the example we have a list with 7 elements (original Justice League characters), each element contains the character and the pointer to the next character which most of the time were not allocated in adjacent blocs.
> > > [("Superman","12"),("Batman","B2"),("Wonder Woman","13"),("The Flash","33"),("Green Lantern","E3"),("Aquaman","97"),("Martian Manhunter","Null")]
> > > Why use Linked Lists?
> > > Every data structure has its own set of advantages and disadvantages and one must consider many factors in order to use it effectively. Linked Lists are not an exception, and their use is not recommend for every situation, here are some of its strengths.
> > > Advantages
> > > Saves Memory - Since you don't have to allocate the size of the list before hand, it only uses what it needs.
> > > Dynamic Data Structure - Since elements don't have to be included sequentially you don't have to set a initial size to the List, it can grow and shrink at runtime, by allocating and deallocating memory.
> > > Constant times for Insertion(prepend only) and deletion, O(1), in contrast with Arrays O(n), with Linked List you don't have to shift elements when inserting or deleting to the list. You only have to set the elements with the correct pointers, and you are set to go.

Disavantages
Uses More Memory - Since every element holds its own data and pointer for the next element, and in the case of Doubly-Linked-Lists another pointer for the previous element, it requires more memory.
Linear Time for Traversal - That's the biggest drawback of LinkedLists, since it does not contain indexes, you have to traverse every single element of the list in order to reach its tail O(n), traversing in reverse its even more difficult, since you have to go to the end and then back, unless you are using Doubly-Linked-Lists, but then you are using more memory.
Linear Time for Insertion and deletion - LinkedLists have a linear Time for Insertion and deletion for location based elements. You first have to traverse to the desired element and then perform the action.

Implementing LinkedLists in Python

Now that you saw what are linked lists, and where to use them, let's implement a Linked List using Python. First we need to create an Element class or node if you prefer, that will receive some value and can hold the pointer for the next element or node.

# Creates new Class element that receives value, and holds pointer #for next element, initially next is set to 'None'

> > > class Element(object):
> > > def **init**(self, value):
> > > self.value = value
> > > self.next = None
> > >
> > > node1 = Element("Superman")
> > > print (node1.value) #>>> Superman
> > > print (node1.next) # >>> None
> > > Now that we have a Element class let's create a LinkedList Class to hold the elements and also contain some methods to manipulate them. To begin with, lets just create a class that will receive a node and save it as a head.

# Creates a class LinkedList that will receive a Node and hold it as #head

> > > class LinkedList(object):
> > > def **init**(self, head=None):
> > > self.head = head

> > > justiceLeague=LinkedList(node1)
> > > print (justiceLeague.head.value) #>>> Superman
> > > print (justiceLeague.head.next) #>>> None
> > > Great, now we can create a new Node and also create and Initialize a new LinkedList with that Node. Let's implement an Append method that will insert one element to the end of our list. This method won't be very efficient, since it will have to traverse the entire list before inserting the new element, so time complexity will be linear O(n). Let's get to it.
> > > class LinkedList(object):
> > > #Original code
> > > ...
> > > #Will receive new element and insert it to the end of the list.
> > > def append(self, new_element):
> > > current = self.head
> > > #If our list contains any element, will start traversing it until #last element is found and then set last node.next to the new element, otherwise, just set new_element to the head.
> > > if self.head:
> > > while current.next:
> > > current = current.next
> > > current.next = new_element
> > > else:
> > > self.head = new_element
> > > #-----------------------------//--------------------------------
> > > justiceLeague=LinkedList()
> > > node1 = "Superman"
> > > node2 = "Batman"
> > > justiceLeague.append(node1)
> > > print justiceLeague.head.value #>>> Superman
> > > print justiceLeague.head.next #>>> None

> > > justiceLeague.append(node2)
> > > print justiceLeague.head.next.value #>>> Batman
> > > print node1.next #>>> Batman
> > > Let's create another method that will return the element at a certain position. This too, will have a linear time since we will have to traverse all elements until the position we want O(n).
> > > class LinkedList(object):
> > > #Original code
> > > ...

# will receive position location, create a counter and start #traversing all elements, until location is reached, if position #does not exist, returns None

> > > def get_position(self, position):
> > > current = self.head
> > > counter = 1
> > > while counter <= position and current:
> > > if counter == position:
> > > return current
> > > current = current.next
> > > counter += 1
> > > return None
> > > #-----------------------------//--------------------------------
> > > node3 =Element("Wonder Woman")
> > > node4 = Element("The Flash")
> > > node5 = Element("Green Lantern")
> > > justiceLeague.append(node3)
> > > justiceLeague.append(node4)
> > > justiceLeague.append(node5)
> > > print justiceLeague.get_position(1).value #>>> Superman
> > > print justiceLeague.get_position(3).value #>>> Wonder Woman
> > > print justiceLeague.get_position(5).value #>>> Green Lantern
> > > Great, what about if you create a new method to insert a new node to a specific location? Let's try this. Again, this will be linear time O(n) because we still have to traverse the elements to find the desired position, but we don't have to shift items around after it's found, our method will receive the new_element and a position, it can also be seen as a search time + O(1 ).
> > > class LinkedList(object):
> > > #Original code
> > > ...
> > > #Insert new node at position. If LinkedList has just one element, #set new_element.next with current head.next, and set new_element as #the new head. Otherwise, find element at specified position, insert #it there.
> > > def insert(self, new_element, position):
> > > if position > 1:
> > > target_position = self.get_position(position - 1)
> > > new_element.next = target_position.next
> > > target_position.next = new_element
> > > else:
> > > new_element.next = self.head
> > > self.head = new_element
> > > #-----------------------------//--------------------------------
> > > node6 = Element("Aquaman")
> > > justiceLeague.insert(node6,3) # insert Aquaman to position 3
> > > print justiceLeague.get_position(1).value #>>> Superman
> > > print justiceLeague.get_position(3).value #>>> Aquaman
> > > print justiceLeague.get_position(4).value #>>> Wonder Woman
> > > Let's implement a delete method now. The delete method is very similar to the insert, the only difference is that instead of add the item, we will be deleting it, so our method only needs the value, O(n), since we have to traverse our list looking for the correct value, it can also be seen as a search time + O(1).
> > > class LinkedList(object):
> > > #Original code
> > > ...

# method takes a value and traverses the list, if value is found it #deletes it and set the pointer to the previous element, if not #found returns False

> > > def delete(self, value):
> > > current = self.head
> > > previous = None
> > > while current:
> > > if current.value == value:
> > > if not previous:
> > > self.head = current.next
> > > return True
> > > else:
> > > previous.next = current.next
> > > return True
> > > previous = current
> > > current = current.next
> > > return False
> > > #-----------------------------//--------------------------------
> > > node7 =Element("Green Arrow")
> > > justiceLeague.insert(node7,5) # insert Green Arrow to position 5
> > > print justiceLeague.get_position(5).value #>>> Green Arrow
> > > justiceLeague.delete("Green Arrow")
> > > print justiceLeague.get_position(5).value #>>> The Flash
> > > print justiceLeague.delete("Green Arrow")#>>> False
> > > Ok, now let's add two more methods insert_first and delete_first, this time around our time complexity would be constant O(1), since we don't have to traverse nor shift anything. That's great isn't it?
> > > class LinkedList(object):
> > > #Original code
> > > ...

# Insert will receive a new_element and set it as the new Head, #updating its next to the previous value.

def insert_first(self, new_element):
new_element.next = self.head
self.head = new_element
return self
#Delete will just delete the first item, setting the second element #as the new head.
def delete_first(self):
if self.head:
deleted = self.head
self.head = self.head.next
deleted.next = None
return deleted
#-----------------------------//--------------------------------

> > > node7 =Element("Martian Manhunter")
> > > node8=Element("Green Arrow")
> > > justiceLeague.insert_first(node7)
> > > justiceLeague.insert_first(node8)
> > > print justiceLeague.get_position(1).value #>>> Green Arrow
> > > print justiceLeague.get_position(2).value #>>> Martian Manhunter
> > > print justiceLeague.delete_first().value #>>> Green Arrow
> > > print justiceLeague.get_position(2).value #>>> Superman
> > > print justiceLeague.get_position(1).value #>>> Martian Manhunter
> > > Ok, now you have it. We pretty much cover everything, well not quite, we still need a method count, a method list, and many more, but I think now you can take it from here, and implement it yourself.
> > > Linked lists don't have much use in python, and many other languages, because most higher programming languages already include constructs that deal with it. But, linked list is a very important concept in Computer Science and some languages like C, C++. Linked Lists are also a very popular topic in technical interviews.

