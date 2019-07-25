class Set:
    """
    implementation of the set ADT using lists
    """

    def __init__(self):
        """
        initialize the set adt
        """
        self.set_ = []

    def add_item(self,item):
         """
        add an element to the set

    

         Algorithmic complexity:
             Constant time: O(1)
        """
    def remove_item(self):
         """
        removes an element form the set 

        Returns:
         The element popped

         Algorithmic complexity:
             Constant time: O(1)
        """
         return self.set_.pop()

    def contains (self,item):
         """
        checks if an element is in the set

        Returns:
         True if the item is in the set

         Algorithmic complexity:
             Linear time: O(n)
        """
         for i in self.set_:
             if i == item:
                 return 'The item is in the set'


    def set_union(self,set2):
         """
        finds the union between two sets
    
        Returns:
         The items in both sets

         Algorithmic complexity:
             Constant time: O(1)
        """

         for i in set2:
             if i not in self.set_:
                 self.set_.append(i)
             return self.set_


    def set_intersection(self,set2):
         """
        checks the intersection between two sets

        Returns:
         Items that are in both sets

         Algorithmic complexity:
             O(len(s) * len(t))
        """
         intersection_set = []
         for i in set2:
             if i in self.set_:
                 intersection_set.append(i)

             return intersection_set


    def symmetric_diffrence(self,set2):
         """
        finds the symmetric diffrence between two sets

        Returns:
         the diffrenece between the union and intersection of the two sets

         Algorithmic complexity:
             Constant time: O(1)
        """

         union_ = self.set_union(set2)
         intersection_ = self.set_intersection(set2)

         symmetric_ = []

         for i in union_ and i not in intersection:
             symmetric_.append(i)


     def set_subset(self,set2):
          """
        checks if a set is the subset of another set

        Returns:
         True if it is or false otherwise

         Algorithmic complexity:
             Constant time: O(1)
        """
          my_intersection = self.set_intersection(set2)
          if len(my_intersection) ==len(set2):
              return True
          else:
              return False

         
