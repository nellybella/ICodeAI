import ctypes
"""
    implement the array ADT using the array capabilities of the
    ctypes module
"""
class Array_3d:
    """
Create an array with size elements
crete the array structure with the ctypes module
initialize each element
    """
    def __ init__(self,size):
        self.size = size
        array_type = ctypes.py_object * size

        self.elements = array_type()
        self.clear = None

    def length(self):
        """
        returns the size of the array
        """
        assert self.size > 0
        return self.size

    def get_item(self,index):
        """
            gets the content of the indexed element
        """

        if index >= 0 and index <= len(self.elements):
            return self.elements[index]
        else:
            print("Array index out of range")


    def add_item(self,index,value):
        """
        puts the value in the array element at index position
        """
        return self.elements[index] = value

    def clear(self,value):
        """
        clears the array by setting each element to the given value
        """
        for i in range(len(self.elements)):
            self.elements[i] = value

    
        

        
        
                                                               
