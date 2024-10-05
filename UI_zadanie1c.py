from array import array
from copy import deepcopy
from threading import get_native_id
from typing import OrderedDict
from time import *

class Node:
    def __init__(self, parent, array):
        self.parent=parent                      #potrebujem si pamätať parent node najmä pri vypisovaní
        self.left=None                          
        self.right=None
        self.down=None
        self.up=None
        self.array=array                        #informácie o hlavolame, to si iba pamätám aby som to nemusel si túto informáciu pamätať inde v programe
        self.size_row=len(array)
        self.size_col=len(array[0])



#do stacku vkladám všetky nové vytvorené nody na koniec pomocou funkcie _push() cez .append(). 
#ďalej v programe porovnávam stavy s počiatočného a koncového stavu.
#keď nenájdem zhodu tak uzol zo stacku vyhodím a pokračujem ďajel v hľadaní riešenia. vyhodený uzol potom následne porovnávam ďalej
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


#tuná si najmä pamätám počiatoční a koncový stav a ich informácie

class Hlavolam:

    def __init__(self, root_starting, root_ending):
        self.timer_start = process_time()

        self.root_starting=root_starting
        self.root_ending=root_ending        
        self.size_row=len(root_starting.array)
        self.size_col=len(root_starting.array[0])
        self.stack_front=Stack()
        self.stack_back=Stack()
        self.stack_front._push(self.root_starting)
        self.stack_back._push(self.root_ending)


    #táto funkcia slúži na prechádzanie hlavolamom, t.j. jeho riešením
    def _search(self):
        while not self.stack_front._isEmpty() and not self.stack_back._isEmpty():  #pokiaľ stack nie je prázdny tak viem že tam mám stavy na porovanie
            current_node = self.stack_front._pop()      #cez pop si získam uzol na porovnanie
            row=0
            col=0
            for i in range(self.size_row):
                for j in range(self.size_col):
                    if current_node.array[i][j]=='m': #nájdem si pozíciu prázdneho miesta. potrebujem jeho index pre stĺpec a riadok
                        row=i
                        col=j


    #prvý riadok v 2d poli (t.j horný) je indexovaný nulou. to isté platí pre prvý stĺpec (t.j. ľavý). túto informáciu využijem pri 
    #prechádzaním hlavolamu. pozriem sa, čí m mi nevyskočí z 2d polia a keď nie, tak ho posuniem. potom cez funkciu _swap() získam nový stav
    #a ten hodím do stacku. potom porvnávam stavy. keď nájdem zhodu, vypíšem

            #idem HORE 
            if row-1 >=0:
                current_node.up=Node(current_node,self._swap(row-1, col, row, col, current_node.array))
                self.stack_front._push(current_node.up)
                match_dictionary=self._compare_matrix(current_node.up,self.stack_back)
                if len(match_dictionary)==2: #informácie sú uložené v slovníku kde mám dva kľuče. pokiaľ nemám zhodu tak vrátim prázdny slovník bez kľučov
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break

            #idem DOLE
            if row+1 < self.size_row:
                current_node.down=Node(current_node,self._swap(row+1, col, row, col, current_node.array))
                self.stack_front._push(current_node.down)
                match_dictionary=self._compare_matrix(current_node.down,self.stack_back)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break

            #idem DOLAVA
            if col-1 >=0:
                current_node.left=Node(current_node,self._swap(row, col-1, row, col, current_node.array))
                self.stack_front._push(current_node.left)
                match_dictionary=self._compare_matrix(current_node.left,self.stack_back)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break

            #idem DOPRAVA 
            if col+1 < self.size_row:
                current_node.right=Node(current_node,self._swap(row, col+1, row, col, current_node.array))
                self.stack_front._push(current_node.right)
                match_dictionary=self._compare_matrix(current_node.right,self.stack_back)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break
    
    #vyriesil som jedno porovnanie pre cestu s *pociatocneho* stavu. teraz treba spraviť to isté pre koncový stav
    #princíp je presne taký istý, ako riešenie pre stavy s počiatočného stavu, iba to riešim pre koncový stav       
            current_node = self.stack_back._pop()
            row=0
            col=0
            for i in range(self.size_row):
                for j in range(self.size_col):
                    if current_node.array[i][j]=='m':
                        row=i
                        col=j

            #idem HORE 
            if row-1 >=0:
                current_node.up=Node(current_node,self._swap(row-1, col, row, col, current_node.array))
                self.stack_back._push(current_node.up)
                match_dictionary=self._compare_matrix(current_node.up,self.stack_front)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break
            
            
            #idem DOLE
            if row+1 < self.size_row:
                current_node.down=Node(current_node,self._swap(row+1, col, row, col, current_node.array))
                self.stack_back._push(current_node.down)
                match_dictionary=self._compare_matrix(current_node.down,self.stack_front)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break


            #idem DOLAVA
            if col-1 >=0:
                current_node.left=Node(current_node,self._swap(row, col-1, row, col, current_node.array))
                self.stack_back._push(current_node.left)
                match_dictionary=self._compare_matrix(current_node.left,self.stack_front)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break

            #idem DOPRAVA 
            if col+1 < self.size_row:
                current_node.right=Node(current_node,self._swap(row, col+1, row, col, current_node.array))
                self.stack_back._push(current_node.right)
                match_dictionary=self._compare_matrix(current_node.right,self.stack_front)
                if len(match_dictionary)==2:
                    print("nasla sa zhoda")
                    self._print_solution(match_dictionary)
                    break
    
    #funckia kde posuniem m 
    def _swap(self, row, col, row_m, col_m, array):
        temp_array = deepcopy(array)
        temp=temp_array[row][col]
        temp_array[row][col] = temp_array[row_m][col_m]
        temp_array[row_m][col_m] = temp
        return temp_array

    def _solver(self):
        while not self.stack_front._isEmpty():
            tempStackPop = self.stack_front._pop()
            row=0
            col=0
            for i in range(0,self.size_row):
                for j in range(0, self.size_col):
                    if tempStackPop.array[i][j] == 'm':
                        row=i
                        col=j  

    #v tejto funckii porovnam stavy a hľadám zhody
    def _compare_matrix(self, node, stack):
        matrix=node.array
        stack=stack.stack

        for n in stack:   #for cyclus iba na kontrolu či stavy sú v poriadku
            temp_matrix=n.array
            if n.size_row != node.size_row:
                return {}
            if n.size_col != node.size_row:
                return {}
            
            counter = 0 #na pocitanie identickych prvkov v matici
            
            for i in range(0,n.size_row): #hladám zhody
                for j in range(0,n.size_col):
                    if matrix[i][j] == temp_matrix[i][j]:
                        counter += 1
            
            if (n.size_row * n.size_col) == counter:  #su zhodne, tak vrátim slovník s 2 klucmi
                return {
                    "First_node": node,
                    "Second_node": n
                }        

        return {} #nenašiel som zhodu, tak vrátim prázdny sklovník
    
    def _print_solution(self, match_dic): #funckia na výpis
        print("\n")
        steps_counter =0
        temp=match_dic["First_node"]

        while temp is not None:
            print(temp.array)
            temp = temp.parent
            steps_counter +=1
            
        temp=match_dic["Second_node"]

        print("*** *** ***")
        print("Vypisujem druhu polovicu")
        print("*** *** ***")
        
        while temp is not None:
            print(temp.array)
            temp = temp.parent
            steps_counter +=1

        time_stop = process_time()

        print("Cas: ", time_stop-self.timer_start)   #zastavím čas
        print("Pocet krokov: ", steps_counter)       #a vypíšem kroky

def _check_if_solvable(arr_starting):
            inv_count = _get_inv_count([j for sub in arr_starting for j in sub])

            return (inv_count % 2 == 0) 

def _get_inv_count(arr):
    inv_count = 0
    empty_value = 'm'
    for i in range(0,9):
        for j in range(i + 1,9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

            
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

    root_starting=Node(None,arr_starting)
    root_ending=Node(None, arr_ending)
    hlavolam = Hlavolam(root_starting, root_ending)
    hlavolam._search()
