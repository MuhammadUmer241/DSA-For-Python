
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

    def insertion_sort(self)->list[int]:
        """

        :return: sorted list
        """

        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key

        return self.array

    def quick_sort(self,array):
        """

        :param array:
        :return:
        """
        if len(array) <= 1:
            return array
        pivot = array[0]

        partition_left = [array[val] for val in range(len(array)) if array[val] < array[0]]
        partition_right = [array[val] for val in range(len(array)) if array[val] > array[0]]

        return self.quick_sort(partition_left) + [pivot] + self.quick_sort(partition_right)


     






