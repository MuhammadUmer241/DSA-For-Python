
class sorting:
    def __init__(self,array:list[int]):
        self.array= array

    def bubble_sort(self)->list[int]:
        """
        Sorting the array by bubble sort
        :param array:
        :return: sorted array
        """
        n= len(self.array)
        for i in range(n):
            for index in range(n-1):
                if self.array[index]>self.array[index+1]:
                    self.array[index], self.array[index+1]= self.array[index+1],self.array[index]

        return self.array





obj= sorting([23,13,29,19,21])
print(obj.bubble_sort())