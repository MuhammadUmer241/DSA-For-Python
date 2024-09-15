class Node:
    """
    Blue print for a Node
    """
    def __init__(self,value):
        self.data= value # value of current node
        self.next= None # address of last node

class linked_list:
    """
    contains methods used in linked list to insert delete , Find etc
    """
    def __init__(self):
        self.head =None
        self.n= 0



    def insert_head(self,value:any)->None:
        """
        method to add node by head
        :param value:
        :return: None
        """
        new_node= Node(value) #initialize new node
        new_node.next= self.head #contains address of last node
        self.head= new_node
        self.n= self.n +1
        print(new_node.next, self.head)


    def insert_tail(self,value:any)->None:
        """
        method to insert node by tail

        :param value:
        :return:
        """
        new_node= Node(value)
        if self.head == None:
            self.head= new_node
            self.n= self.n + 1
            return
        curr = self.head
        while curr.next!= None:
            curr= curr.next

        curr.next= new_node
        self.n = self.n +1



    def insert_after(self, after:any, value:any)->None:
        """
        Method to insert value after a certain value
        :param after:
        :param value:
        :return:
        """
        new_node= Node(value)
        curr = self.head

        while curr.data!= after:
            curr= curr.next
            if curr.next.next==None:
                # if we are going to insert value after tail
                break

        new_node.next= curr.next
        curr.next= new_node
        self.n = self.n +1



    def delete_head(self)->None:
        """
        delete the head
        :return: None
        """
        if self.head==None:
            # Our list is empty
            print("list is empty")


        self.head= self.head.next
        self.n = self.n -1

    def delete_tail(self)->None:
        """
        Delete Tail of the Node
        :return:
        """
        curr= self.head

        if curr.next == None:
            # if this block is executed it means we have only one node in it and we are going to delete it
            return  self.delete_head() # already created func to delete the head

        while curr.next.next != None:
            curr= curr.next

        curr.next= None
        self.n= self.n-1

    def delete_after(self,after:any)->None:
        """
        deleter the value
        :param after:
        :return:
        """
        curr= self.head

        while curr.data!=after:
            curr = curr.next
            if curr.next.next==None: # case to handle if value is tail
                break


        curr.next= curr.next.next
        self.n = self.n-1

    def find(self, value)->None:
        """
        print index of given value
        :param value:
        :return: None
        """
        pos= 0
        curr= self.head
        # print(curr.next)
        while curr != None:
            if curr.data==value:
                 return print("Item on", pos)
            curr = curr.next
            pos = pos + 1
        return print("Index Not found")


    def __str__(self)->str:
        curr = self.head
        result = ''


        while curr != None:
            result = result + str(curr.data) + "->"
            curr = curr.next


        return result[:-2]

obj = linked_list()
obj.insert_head(1)
print(obj)
obj.insert_tail(3)
obj.insert_after(1,4)
obj.insert_after(4,5)
print(obj)
obj.insert_after(6,6)
print("Node after insertion Test",obj)
obj.delete_after(3)
print("Node after deletion Test",obj)
obj.find(9)
obj.find(4)
print(obj)


