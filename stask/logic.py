import random

import conf


class Cell:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.in_square = False


    def is_neighbor(self, cell, color):
        if cell.color == color:
            if (cell.x in range(self.x-conf.RADIUS, self.x+conf.RADIUS+1) and
                    cell.y in range(self.y-conf.RADIUS, self.y+conf.RADIUS+1)):
                return True

        return False


    def has_neighbors(self, table):
        for cell in table:
            if self.is_neighbor(cell, conf.DEFECT_COLOR):
                return True
        return False


    def pour(self, table):
        for i in range(len(table)):
            if self.is_neighbor(table[i], conf.MAIN_COLOR):
                table[i].color = conf.POUR_COLOR
        return table


class Table:
    def __init__(self, x=0, y=0, use_config_file=True):
        if use_config_file:
            self.x = conf.TABLE_X
            self.y = conf.TABLE_Y
        else:
            self.x = x
            self.y = y
        self.table = None
        self.init_table()


    def init_table(self):
        table = []
        for i in range(self.y):
            for j in range(self.x):
                table.append(Cell(j, i, conf.MAIN_COLOR))
        self.table = table


    def defect(self):
        table = self.table
        for i in range(len(table)):
            table[i].color = random.choice([conf.MAIN_COLOR]*15 + [conf.DEFECT_COLOR])
        self.table = table

    
    def run(self):
        table = self.table
        for cell in table:
            if cell.color == conf.DEFECT_COLOR and cell.has_neighbors(table):
                self.table = cell.pour(table)




