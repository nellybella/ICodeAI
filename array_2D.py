class myArray:
    def __init__(self,no_rows,no_cols):
        self.rows = no_rows
        for i in range(no_rows):
            self.rows[i] =no_cols

    def no_rows(self):
        return len(self.rows)

    def no_cols(self):
        return len(self.rows[0])

    def clear_arr(self,value):
        for row in self.rows:
            row.clear_arr(value)

    def getitem(self,index_,value):
          #no of array subscripts
            row = index_ [0]
            col = index_ [1]
            if row > self.no_rows and col > self.no_cols:
                raise IndexError ('invalid index')
            arr_index = self.rows[row]
            return arr_index[col]


    def setitem(self,index_,value):

        row = index_ [0]
        col = index_ [1]
        if row > self.no_rows and col > self.no_cols:
            raise IndexError ('invalid index')
        arr_index = self.rows[row]
        arr_index[col] = value




