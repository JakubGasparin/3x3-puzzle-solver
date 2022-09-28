from array import array
from copy import deepcopy


class Hlavolam:
    def __init__(self, root):
        pass

class Node:
    def __init__(self, parent, array, size_row, size_col):
        self.parent=parent
        self.left=None
        self.right=None
        self.down=None
        self.up=None
        self.array=array
        self.size_row=size_row
        self.size_col=size_col


    def _search(self):
        print(self.array, self.size_row, self.size_col)
        row=0
        col=0
        for i in range(self.size_row):
            for j in range(self.size_col):
                if self.array[i][j]=='m':
                    #print("found m")
                    #print(i,j)
                    row=i
                    col=j

        print(row, col)

        #idem HORE 
        if row-1 >=0:
            print("swapping up...")
            self._swap(row-1, col, row, col)
        
        #idem DOLE
        if row+1 < self.size_row:
            print("swapping down...")
            self._swap(row+1, col, row, col)

        #idem DOLAVA
        if col-1 >=0:
            print("swapping left...")
            self._swap(row, col-1, row, col)
        else: 
            print("cant move left")

        #idem DOPRAVA 
        if col+1 < self.size_row:
            print("swapping right...")
            self._swap(row, col+1, row, col)
        else: 
            print("cant move right")
        
        
    
    def _swap(self, row, col, row_m, col_m):
        temp_array = deepcopy(self.array)
        temp=temp_array[row][col]
        #print(temp, row, col, row_m, col_m)
        temp_array[row][col] = temp_array[row_m][col_m]
        temp_array[row_m][col_m] = temp
        print(temp_array)
        return temp_array
       
        





if __name__ == "__main__":
    arr=[]  
    rows, cols=3,3
    for i in range(rows):
        col = []
        for j in range(cols):
            value=input()
            col.append(value)
        arr.append(col)
    #print(arr)
    t=Node(None,arr, rows, cols)
    t._search()




    #char = input("enter your hlavolam: ")
    #counter=1
    #arr_col=[]
    #for i in char: #range(1,10):
        #print(i)
        #arr_row=None
        #if i=='(' and arr_row == None:
         #   arr_row=[]
          #  print(arr_row)
           # continue
        #if type(arr_row)==type(list()) and (i!='(' and i!=',' and i!=')') :
         #   arr_row.append(i)
          #  print(arr_row)
           # continue
       # if i==')':
        #    print(arr_row)
         #   arr_col.append(arr_row)
          #  arr_row=None
           # continue
        #counter=counter+1
    #print(hlavolam)
    #print(char)
    #print(arr_col)

