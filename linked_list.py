class Node:
    """
    a linked list node to store a stack entry
    """
    def __init__(self,element):
        self.element = element
        self.next = None

    class Stack:
        """
        A class to represent a stack
        """
        def __init__(self):
            self.head = None


        def is_empty(self):
            """
        checks if the stack is empty

        Returns:
         True if the stack is empty and false otherwise

         Algorithmic complexity:
             Constant time: O(1)
        """

            return self.head == 0



        def push(self):
             """
        adds a node to the front of the linked list

        Returns:
         linked list with a node if the stack was empty

         Algorithmic complexity:
             Constant time: O(1)
        """
            if self.head == 0:
                self.head = Node(element)

            else:
                self.head = Node(element)
                new_node.next = self.head
                self.head = new_node  

        def pop(self):
             """
        removes the node at the front of the linked list

        Returns:
         the data of the node at the front of the stack and removes
         the node.
         It returns none if there are no nodes

         Algorithmic complexity:
             Constant time: O(1)
        """
            if self.is_empty() == False:
                return  None
            else:
                item_popped = self.head.element
                self.head = self.head.next

                return item_popped

            
        def length(self):
             """
        checks length of the stack

        Returns:
         the number of items in the stack

         Algorithmic complexity:
             Constant time: O(1)
        """
             return len(self.head)



    
