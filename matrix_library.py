from copy import deepcopy

def print_matrix(matrix):
    for row in range(len(matrix)):
            print matrix[row]       

def sum_of_matrices(matrix_a, matrix_b):
    matrix_result = deepcopy(matrix_a)
    for row in range(len(matrix_a)):
        for column in range(len(matrix_a[row])):
            matrix_result[row][column] += matrix_b[row][column]
    return matrix_result  

def multiply_of_matrices(matrix_a, matrix_b):
    matrix_result = deepcopy(matrix_a)
    for row_a in range(len(matrix_a)):
        for column_a in range(len(matrix_a[row_a])):
            sum_of_multiplications = 0
            for column_b in range(len(matrix_b[column_a])):
                sum_of_multiplications += matrix_a[row_a][column_a]*matrix_b[row_a][column_b] 
            matrix_result[row_a][column_a] = float("{0:.2f}".format(sum_of_multiplications))
    return matrix_result    

class Matrix_representator(object):
    def __init__(self, matrix_NxN):
        self.matrix_data = matrix_NxN
        print_matrix(self.matrix_data) 
    def add(self, other_matrix_object):
        return sum_of_matrices(self.matrix_data, other_matrix_object.matrix_data)
    def multiply_with(self, other_matrix_object):
        return multiply_of_matrices(self.matrix_data, other_matrix_object.matrix_data)




