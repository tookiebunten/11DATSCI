""""Receives two lists of numbers of length m, and m * n, respectively. Values 
at index i of the first list are multiplied by values at index j in the second list, 
where j = i * n. Two examples are illustrated, here: 

list one 2,8,9,5,3
list two 1,4,2,9,5,9,8,9,3,0
n=2
2x1, 8x2, 9x5, 5x8, 3x3

list one 9,5,6,7,3
list two 3,2,7,5,2,9,7,2,1,9,6,9,3 
n=3
9x3, 5x5, 6x7, 7x9, 3x3
 
You must implement the solution for arbitrary values of n and handle 
incompatible list sizes by returning an empty list."""