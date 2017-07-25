'''
Selection Sort  -
In selection_sort, one element is checked against all other elements of the list and replaced with the element smaller than it.
selection_suffix increments once the smallest element comes to the left of the list. We can say, list from beginning to selection_suffix is sorted.
The sorted element is present in the left and the comparison does not include an element once it is present in the sorted part of the list.
L[:selection_suffix] is always sorted.

'''

def selection_sort(L):
    selection_suffix = 0            #This is the element next to the sorted element in the list
    while selection_suffix != len(L):
        for i in range(selection_suffix, len(L)):
            if L[selection_suffix] < L[i]:          #selection_suffix increments once the smallest element comes to the left of the list.
            L[i], L[selection_suffix] = L[selection_suffix], L[i]

        selection_suffix += 1
