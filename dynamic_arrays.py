import ctypes

class dynamic_array:
    def __init__(self):
        """
        dynamic_array is class to handle problems cause by array , as we know array have fixed shape which can
        be an issue in order to dealing with  values dynamically increasing or decreasing
        """
        self.n= 0 # number of chr
        self.size= 1 # size/len of array
        self.A= self.__create_array(self.size)

    def __str__(self)->str:
        """
        method to return array in desired shape
        :return: str
        """
        result = ""
        for i in range(self.n):
            result= result+ str(self.A[i]) + ","
        return "["+result[:-1]+"]"

    def __delitem__(self, key:int)->None:
        """
        delete the value on given index
        :param key:
        :return:
        """

        self.__index(key)
        for i in range(key,self.n-1):
            self.A[i] = self.A[i+1]

        self.n= self.n-1

    def insert(self,pos:int, item:any )->None:
        """
        Insert item on specified position and push value the old value one step ahead
        :param pos:
        :param item:
        :return: None
        """
        self.__index(pos) # private method to raise error if number of items is greater then the position provided
        if self.n == self.size:
            self.__resize_array(2 * self.size)

        for i in range(self.n, pos, -1):
            self.A[i]= self.A[i-1] # creating a position according to "pos" to append item there

        self.A[pos]= item
        self.n= self.n+1


    def __index(self, pos:int)->None:
        """
        raise an error when
        :param pos:
        :return: None
        """
        if self.n<pos:
            raise "index-out-of-range"
    def __len__(self):
        """
        number of elements in array
        :return: None
        """
        print(self.n)


    def pop(self)->None:
        """
        Pop the last item
        :return: None
        """
        if self.n==0:
            print("Empty List")
        else:
            print(self.A[:self.n-1])
            self.n=self.n-1

    def append(self,item:any)->None:
        """
        append item to the last
        :param item:
        :return: None
        """
        if self.size== self.n:
            self.__resize_array(self.size*2)
        self.A[self.n]= item  # append value to last index
        self.n = self.n + 1


    def __resize_array(self,size:int)->None:
        """
        create an array B to extend the size of array A by replacing B by A
        :param size:
        :return: None
        """
        B= self.__create_array(size)
        self.size= size
        for values in range(self.n):
            B[values]= self.A[values]
        self.A= B

    def __create_array(self, size):
        """
        using a C library to create a C array
        :param size:
        :return: array of given size
        """
        return (size * ctypes.py_object)()





my_list= dynamic_array() #making instance
print("Empty ", my_list)
my_list.append("Muhammad") #append string
my_list.append(2) # append int
my_list.append(True) #append bol
print("Append ", my_list)
my_list.insert(3,"Pakistan") #insert value
print("Insert ", my_list)
my_list.__delitem__(1)
print("Del ", my_list)
my_list.pop()

print("pop",my_list)
