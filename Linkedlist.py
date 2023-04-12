from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
#função para adicionar elementos ao fim da lista
    def append(self, element, priori):
        self.prioridade = priori
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
        if self.prioridade == 1:
            lista.insert(0, self.element)
        elif self.prioridade == 2:
            pass
        elif self.prioridade == 3:
            lista.insert(len(lista)-1,self.element)
        
    def priority(self,element, priori):
        self.element = element
        self.prioridade = priori   
        if self.prioridade == 1:
            lista.remove(self.element)
            lista.insert(0,self.element)
        elif self.prioridade == 3:
            lista.remove(self.element)
            lista.insert(len(lista)-1, self.element)
        elif self.prioridade == 2:
           pass

#Função para ler tamanho de lista e retornar   
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
#funções para poder utilizar a lista encadeada como se fosse uma lista normal    
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
#função que lê endereço de determinado elemento    
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

#Função para inserir elementos dentro da lista em qualquer posição desde que não seja maior que o len(lista)
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
                   

#Função para printar todos os elementos da lista em ordem       
    def show(self):
        c = 0
        print('-----lista de atividades-----\n')
        for i in lista:
              
            print(f'{c}- {i}')
            c = c + 1
#função para confirmar que uma tarefa foi feita
    def check(self, index, element):
        result = ''
        for i in element:
            result = result + i + '\u0336'
 #       lista.replace(index, result)
        lista.insert(len(lista), result)
        lista.remove(element)
        
        return lista.show()
#função para remover itens de dentro da lista
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

#loop do menu:


while True:
    entrada = input("\n---TO DO LIST---\n\nMenu:\n1- Adicionar na lista\n2- Atividade feita\n3- Mostrar lista\n4- Alterar prioridade de atividade\n0- Sair\n\n")

    if entrada ==  "1":
        entrada_append = input("Digite a atividade a  ser adicionada: ").lower()
        prioridade = input("Digite o nível de prioridade do item, sendo 1 o mais alto e 3 o mais baixo: ")
        print('\n')
        lista.append(entrada_append,prioridade)
        lista.show()
        print('\n')
    elif entrada == "2":
        print('\n')
        entrada_index = int(input("Digite o índice da atividade finalizada:"))
        entrada_element = input("Digite a atividade a que foi completada:").lower()
        lista.check(entrada_index, entrada_element)
        print('\n')
    elif entrada == "3":
        print('\n')
        lista.show()
        print('\n')
    elif entrada == "4":
        print('\n')
        entrada = input("digite o elemento a ser alterado a prioridade: ").lower()
        prioridade = int(input("digite o nível de prioridade do item, sendo 1 o mais alto e 3 o mais baixo: "))
        lista.priority(entrada,prioridade)
        lista.show()
        print('\n')

    elif entrada == "0":
        break
    else:
        raise ValueError
    