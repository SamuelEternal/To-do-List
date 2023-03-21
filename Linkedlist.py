from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, element):
        self.element = element
        #add quando a lista já possui head
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        #add quando a lista está vazia
        else:
            self.head = Node(element)
        self.size += 1
    
    def __len__(self):
        #retorna o tamanho da lista
        return self.size
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        return pointer
    
    def __getitem__(self, index):
        # a = lista[6]
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")
    
    def __setitem__(self,index, element):
        # lista[5] = 9
        pointer = self._getnode(index)
        if pointer:
            pointer.data = element
        raise IndexError("list index out of range")     
    
    def index(self, element):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == element:
                return i 
            else:
                pointer = pointer.next
                i += 1
        raise ValueError("{} is not in list" .format(element))
# mostra todas as tarefas listadas



    def insert(self, index, element ):
        node = Node(element)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next  = node
        self._size = self.size +  1    
                   

        
    def show(self):
        c = 0
        print('-----lista de atividades-----\n')
        for i in lista:
              
            print(f'{c}- {i}')
            c = c + 1

    def check(self, index, element):
        result = ''
        for c in element:
            result = result + c + '\u0336'
 #       lista.replace(index, result)
        lista.insert(index, result)
        lista.remove(element)
        return lista.show()
    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list" .format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer = None
                else:
                    ancestor = pointer
                    pointer = pointer.next
            


        

lista = LinkedList()
lista.append('Lavar o carro')
lista.append('Jogar lixo')
lista.append('varrer casa')
lista.append('correr')

while True:
    entrada = input("\n\n---TO DO LIST---\n\n  Menu:\n1- Adicionar na lista\n2- Atividade feita\n3- Mostrar lista\n0- Sair\n")

    if entrada ==  "1":
        entrada_append = input("Digite a atividade a  ser adicionada:")
        print('\n')
        lista.append(entrada_append)
        lista.show()
        print('\n')
    elif entrada == "2":
        print('\n')
        entrada_index = int(input("Digite o índice da atividade finalizada:"))
        entrada_element = input("Digite a atividade a que foi completada:")
        lista.check(entrada_index, entrada_element)
        print('\n')
    elif entrada == "3":
        print('\n')
        lista.show()
        print('\n')
    elif entrada == "0":
        break
    else:
        raise ValueError
        