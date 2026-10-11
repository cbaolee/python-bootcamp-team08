"""
    Transpose of a matrix is a new matrix that is obtained by swapping the rows and columns
    of the given matrix or vice versa.
    For example, [[1, 2, 3], [4, 5, 6]] becomes [[1, 4], [2, 5], [3, 6]].
    
    C++ (vector<vector<int>>): You typically create the output matrix and copy each element
                               using result[column][row] = matrix[row][column].
    Python (list[list[int]]): A nested list comprehension performs the same element swap. 
                              zip(*matrix) is a shorter alternative.
    
    Main differences: C++ requires you to allocate the output and manage its dimensions explicitly. 
                      Python’s zip(*matrix) can make the operation shorter, but it returns tuples and 
                      truncates to the shortest row. Both examples assume the rows have equal lengths; 
                      for ragged rows, decide how you want missing elements handled.
"""
def transpose(matrix : list[list[int]]) -> list[list[int]] :
    if not matrix or not matrix[0] :
        return []
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]
    
"""
    #Using (*zip)
        return [list(row) for row in zip(*matrix)]
        
    Note: zip(*matrix) stops at the shortest row, so if the rows have different lengths, some values are 
    omitted. 
"""