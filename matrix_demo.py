# pip3 install numpy
import numpy


# add() :- This function is used to perform element wise matrix addition.
# subtract() :- This function is used to perform element wise matrix subtraction.
# divide() :- This function is used to perform element wise matrix division.

# initializing matrices
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])

print(f"matrix x : {x}")
print(f"matrix y : {y}")


 # using add() to add matrices
print ("The element wise addition of matrix is : ")
print (numpy.add(x,y))

# using subtract() to subtract matrices
print ("The element wise subtraction of matrix is : ")
print (numpy.subtract(x,y))

# using divide() to divide matrices
print ("The element wise division of matrix is : ")
print (numpy.divide(x,y))



# multiply() :- This function is used to perform element wise matrix multiplication.
# dot() :- This function is used to compute the matrix multiplication, rather than element wise multiplication.
# initializing matrices
x1 = numpy.array([[1, 2], [4, 5]])
y1 = numpy.array([[7, 8], [9, 10]])

# using multiply() to multiply matrices element wise
print ("The element wise multiplication of matrix is : ")
print (numpy.multiply(x1,y1))

# using dot() to multiply matrices
print ("The product of matrices is : ")
print (numpy.dot(x1,y1))


# 6. sqrt() :- This function is used to compute the square root of each element of matrix.
# 7. sum(x,axis) :- This function is used to add all the elements in matrix. Optional “axis” argument computes the column sum if axis is 0 and row sum if axis is 1.
# 8. “T” :- This argument is used to transpose the specified matrix.

# initializing matrices
x2 = numpy.array([[1, 2], [4, 5]])
y2 = numpy.array([[7, 8], [9, 10]])

# using sqrt() to print the square root of matrix
print ("The element wise square root is : ")
print (numpy.sqrt(x2))

# using sum() to print summation of all elements of matrix
print ("The summation of all matrix element is : ")
print (numpy.sum(y2))

# using sum(axis=0) print summation of each column of matrix
print ("The column wise summation of all matrix is : ")
print (numpy.sum(y2,axis=0))

# using sum(axis=1) print summation of each row of matrix
print ("The row wise summation of all matrix is : ")
print (numpy.sum(y2,axis=1))

# using "T" to transpose the matrix
print ("The transpose of given matrix is : ")
print (x2.T)