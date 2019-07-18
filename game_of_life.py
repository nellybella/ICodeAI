import random
class GameOfLife:
     
    def __init__(self,num_cols,num_rows):
        self.num_cols = self.num_cols
        self.num_rows = self.num_rows

        self.active_grid = 0
        self.grids = []


    def create_grid(self):
         rows = []

         for row in range(self.num_rows):
             column_list = [0] * self.num_cols
             rows.append(column_list)
         return row


    def grid_set(self,value=None,grid=0):

        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if value is None:
                    value_cell = random.randint(0,1)
                else:
                    value_cell = value
                self.grids[grid][r][c] = value_cell

    def cell_type(self,row_num,col_name):
        try:
            value_cell = self.grids[self.active_grid][row_num][col_num]
        except:
            value_cell = 0
        return value_cell


    def neighbouring_cell(self,index_row,index_col,get_cell):
        self.get_cell = get_cell

        neighbours_alive = 0
        neighbours_alive += self.get_cell(index_row - 1,index_col - 1)
        neighbours_alive += self.get_cell(index_row - 1, index_col)
        neighbours_alive += self.get_cell(index_row - 1, index_col + 1)
        neighbours_alive += self.get_cell(index_row, index_col - 1)
        neighbours_alive += self.get_cell(index_row, index_col + 1)
        neighbours_alive += self.get_cell(index_row + 1, index_col - 1)
        neighbours_alive += self.get_cell(index_row + 1, index_col)
        neighbours_alive += self.get_cell(index_row + 1, index_col + 1)


        if self.grids[self.active_grid][index_row][index_col] == 1:  # alive
            if neighbours_alive > 3:  # Overpopulation
                return 0
            if neighbours_alive < 2:  # Underpopulation
                return 0
            if neighbours_alive == 2 or neighbours_alive == 3:
                return 1
        elif self.grids[self.active_grid][index_row][index_col] == 0:  # dead
            if neighbours_alive == 3:
                return 1  # come to life

        return self.grids[self.active_grid][index_row][index_col]


    def generation(self):
        """
        Check the current generation, prepare the next generation

        """
        
        self.grid_set(0, self.check_inactive_grid())
        for r in range(self.num_rows - 1):
            for c in range(self.num_cols - 1):
                #next_gen = self.neighbouring_cell(r, c)
                next_gen =self.grids[self.check_inactive_grid()][r][c] 
        self.active_grid = self.check_inactive_grid()
        return next_gen



    def check_inactive_grid(self):
        """
        if the`  active grid is 0 it will return 1 and if the active grid is
        1 it will return 0

        """
        return (self.active_grid +1) % 2






