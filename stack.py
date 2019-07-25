class Stack:
    """
    implemetation of the stack ADT using lists
    
    """
    def __init__(self):
        """ creates an empty stack
        parameter:
        
        
        returns:
        empty stack

     """
        self.items = list()
    def add_item(self,item):
        """
        adds items to the empty stack
        parameter:
            element in the stack

        returns:
            the updated stack with the items
            
        """
        self.items.append(item)
        return self.items 

    def isempty(self):
        """
        checks if the stack is empty

        Returns:
         True if the stack is empty and false otherwise

         Time:
             Constant time: O(1)
        """
         if self.items == []
             return True
        
    def length(self):
        """
         checks the length of the stack

         Parameter:

        Returns:
            the number of elements in the stack

        Time:
            Linear Time : O(n)

        """
        return len(self.items) 
        

    def push_item(self,item):
        """
        push an item to the top of the stack
        parameter:
            the item to be pushed
        Return:
        the stack with the new item at the top

        Time:
            Constant time: O(1)
        """

        return self.append(item)
    

    def remove_item(self):
        """
        removes the top item of the stack

        parameter:

        Return:
        The top item of the stack
        
        Time:
            Constant Time: 0(1)
        """
        try:
            return self.items.pop()

        except IndexError:
            return "The stack is empty"

    def peek_item(self):
        """
        checks the item a the top of the stack without removing it

        parameter:

        Return: the top item

        Algorithmic complexity: O(1)

        """
        if len(self.items != 0):
            return self.items[-1]
            
   
    
