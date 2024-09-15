
class Sorting:
    def __init__(self,array:list[int]):
        self.array= array # array to sort

    def bubble_sort(self)->list[int]:
        """
        Bubble Sort is a simple sorting algorithm that repeatedly
         compares adjacent elements in an array and swaps them if
         they are in the wrong order. This process continues until
         the array is fully sorted. It's a relatively inefficient
         algorithm, especially for large datasets,
         but it's easy to understand and implement

        :return: sorted array
        """

        n= len(self.array)
        for i in range(n): # Iterates according to the length of list
            for index in range(n-1): # Compares adjacent elements and swaps them if needed
                # comparing and swapping if needed
                if self.array[index]>self.array[index+1]:
                    self.array[index], self.array[index+1]= self.array[index+1],self.array[index]

        return self.array





obj= Sorting([23,13,29,19,21])
print(obj.bubble_sort())