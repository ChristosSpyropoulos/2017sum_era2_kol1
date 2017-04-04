from matrix_library import Matrix_representator

print "--------Task1:--------" 
matrix_object1 = Matrix_representator([[1, 2], [3, 4]])
print "" 
matrix_object2 = Matrix_representator([[0.5, 10], [100, 1000]])
print "\n--------Task2:--------" 
matrix_object_of_sum = Matrix_representator(matrix_object1.add(matrix_object2))
print "\n--------Task3:--------"
matrix_object_of_multiply = Matrix_representator(matrix_object1.multiply_with(matrix_object2))
