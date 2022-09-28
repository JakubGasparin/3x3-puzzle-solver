from array import array
from copy import deepcopy

class Node:
    def __init__(self, parent, array):
        self.parent=parent
        self.left=None
        self.right=None
        self.down=None
        self.up=None
        self.array=array
        self.size_row=len(array)
        self.size_col=len(array[0])

class Stack: #LIFO
    def __init__(self): 
        self.stack = []

    def __len__(self):              #funkcia na zistenie velkosti stacku
        return len(self.stack)

    def _push(self,value):
        self.stack.append(value)

    def _pop(self):
        return self.stack.pop(0)

    def _isEmpty(self):
        return len(self.stack) == 0

class Hlavolam:

    def __init__(self, root_starting, root_ending):
        self.root_starting=root_starting
        self.root_ending=root_ending
        self.size_row=len(root_starting.array)
        self.size_col=len(root_starting.array[0])
        self.stack_front=Stack()
        self.stack_back=Stack()
        self.stack_front._push(self.root_starting)
        self.stack_back._push(self.root_ending)

    def _search(self):
        #print(self.array, self.size_row, self.size_col)
        while not self.stack_front._isEmpty() and not self.stack_back._isEmpty():
            current_node = self.stack_front._pop()
            #print(current_node.array)
            row=0
            col=0
            for i in range(self.size_row):
                for j in range(self.size_col):
                    if current_node.array[i][j]=='m':
                        #print("found m")
                        #print(i,j)
                        row=i
                        col=j

            #print(row, col)

            #idem HORE 
            if row-1 >=0:
                #print("swapping up...")
                current_node.up=Node(current_node,self._swap(row-1, col, row, col, current_node.array))
                self.stack_front._push(current_node.up)
                match_dictionary=self._compare_matrix(current_node.up,self.stack_back)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break

            
            
            #idem DOLE
            if row+1 < self.size_row:
               # print("swapping down...")
                current_node.down=Node(current_node,self._swap(row+1, col, row, col, current_node.array))
                self.stack_front._push(current_node.down)
                match_dictionary=self._compare_matrix(current_node.down,self.stack_back)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break

            #idem DOLAVA
            if col-1 >=0:
               # print("swapping left...")
                current_node.left=Node(current_node,self._swap(row, col-1, row, col, current_node.array))
                self.stack_front._push(current_node.left)
                match_dictionary=self._compare_matrix(current_node.left,self.stack_back)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break
            #else: 
               # print("cant move left")

            #idem DOPRAVA 
            if col+1 < self.size_row:
               # print("swapping right...")
                current_node.right=Node(current_node,self._swap(row, col+1, row, col, current_node.array))
                self.stack_front._push(current_node.right)
                match_dictionary=self._compare_matrix(current_node.right,self.stack_back)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break
                  
            #else: 
               # print("cant move right")

            #self.stack_front._print()
        
            current_node = self.stack_back._pop()
            #print(current_node.array)
            row=0
            col=0
            for i in range(self.size_row):
                for j in range(self.size_col):
                    if current_node.array[i][j]=='m':
                        #print("found m")
                        #print(i,j)
                        row=i
                        col=j

           # print(row, col)

            #idem HORE 
            if row-1 >=0:
             #   print("swapping up...")
                current_node.up=Node(current_node,self._swap(row-1, col, row, col, current_node.array))
                self.stack_back._push(current_node.up)
                match_dictionary=self._compare_matrix(current_node.up,self.stack_front)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break
            
            
            #idem DOLE
            if row+1 < self.size_row:
              #  print("swapping down...")
                current_node.down=Node(current_node,self._swap(row+1, col, row, col, current_node.array))
                self.stack_back._push(current_node.down)
                match_dictionary=self._compare_matrix(current_node.down,self.stack_front)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break


            #idem DOLAVA
            if col-1 >=0:
               # print("swapping left...")
                current_node.left=Node(current_node,self._swap(row, col-1, row, col, current_node.array))
                self.stack_back._push(current_node.left)
                match_dictionary=self._compare_matrix(current_node.left,self.stack_front)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break
           # else: 
              #  print("cant move left")

            #idem DOPRAVA 
            if col+1 < self.size_row:
              #  print("swapping right...")
                current_node.right=Node(current_node,self._swap(row, col+1, row, col, current_node.array))
                self.stack_back._push(current_node.right)
                match_dictionary=self._compare_matrix(current_node.right,self.stack_front)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break
          #  else: 
              #  print("cant move right")


         #self.stack_front._print()
        
        
        
    
    def _swap(self, row, col, row_m, col_m, array):
        temp_array = deepcopy(array)
        temp=temp_array[row][col]
        #print(temp, row, col, row_m, col_m)
        temp_array[row][col] = temp_array[row_m][col_m]
        temp_array[row_m][col_m] = temp
        print(temp_array)
        return temp_array

    def _solver(self):
        while not self.stack_front._isEmpty():
            tempStackPop = self.stack_front._pop()
            print(tempStackPop.array)  
            row=0
            col=0
            for i in range(0,self.size_row):
                for j in range(0, self.size_col):
                    if tempStackPop.array[i][j] == 'm':
                        print("found m in stack")
                        #print(i,j)
                        row=i
                        col=j  

    def _compare_matrix(self, node, stack):
        matrix=node.array
        stack=stack.stack

        for n in stack:
            temp_matrix=n.array
            if n.size_row != node.size_row:
                return {}
            if n.size_col != node.size_row:
                return {}
            
            counter = 0 #na pocitanie identickych prvkov v matici
            
            for i in range(0,n.size_row):
                for j in range(0,n.size_col):
                    if matrix[i][j] == temp_matrix[i][j]:
                        counter += 1
            
            if (n.size_row * n.size_col) == counter:  #su zhodne
                return {
                    "First_node": node,
                    "Second_node": n
                }        

        return {}
    
    def _print_solution(self, match_dic):
        print("\n")
        temp=match_dic["First_node"]
        

        while temp is not None:
            print(temp.array)
            temp = temp.parent

        temp=match_dic["Second_node"]

        print("*** *** ***")
        print("Vypisujem druhu polovicu")
        print("*** *** ***")
        
        while temp is not None:
            print(temp.array)
            temp = temp.parent

            
if __name__ == "__main__":
    arr_starting=[]
    arr_ending=[]  
    rows, cols=3,3
    print("Insert starting matrix: \n")
    for i in range(rows):
        col = []
        for j in range(cols):
            value=input()
            col.append(value)
        arr_starting.append(col)

    print("Insert ending matrix: \n")

    for i in range(rows):
        col = []
        for j in range(cols):
            value=input()
            col.append(value)
        arr_ending.append(col)

    #print(arr)
    root_starting=Node(None,arr_starting)
    root_ending=Node(None, arr_ending)
    hlavolam = Hlavolam(root_starting, root_ending)
    hlavolam._search()




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

