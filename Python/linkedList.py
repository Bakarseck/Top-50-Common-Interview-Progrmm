class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_value(self, value):
        self.value = value

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def len(self):
        return self.count

    def InsertBack(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            new_node = Node(value) # On crée un nouveau noeud
            new_node.set_next_node(self.head) # On change l'element vers lequel il pointait en le mettant vers self.head
            self.head = new_node # On met le nouveau noeud comme la tête
            self.count = self.count + 1

    def Search_item(self, value):
        temp = self.head
        while temp != None:
            if value == temp.get_value():
                print("Trouvé")
                return True
            temp = temp.get_next_node()
        print("Non Trouvé")

    def search_at_index(self, index):
        temp = self.head
        compteur = 0
        while temp != None:
            if compteur == index:
                print(temp.get_value())
                return temp.get_value()
            compteur += 1
            temp = temp.get_next_node()
            
    def Print_List(self):
        print("Affichage de la liste ")
        temp = self.head
        while temp != None:
            print(" -> ", temp.get_value(), end=" ")
            temp = temp.get_next_node()


mylist = LinkedList()

for i in range(10):
    mylist.InsertBack(i)

#mylist.Search_item(90)

#mylist.search_at_index(0)

#mylist.return_the_middle()

#print(mylist.len())

#mylist.Print_List()



    

