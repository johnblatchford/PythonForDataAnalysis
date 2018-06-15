""" COMPSCI X433.3 - Python for Data Analysis and Scientific Computing

    John Blatchford - listening@mac.com
    HW2
    1. Include a section with your name
    """

import numpy as np
from numpy import matrix, complex, random, array2string, dot


def hw_2():
    """
    Homework 2
    :return: printouts of the assignement steps and results
    """
    #  2. Create matrix A with size (3,5) containing random numbers A = np.random.random(15)
    a = random.rand(3, 5)
    a = matrix(a)
    a_type = type(a)
    print('\nGenerate a 3,5 matrix of random numbers:\n{0}\nType: {1}'.format(a, a_type))

    #  3. Find the size and length of matrix A
    size_of_a = a.size
    print('\nSize of the matrix: {0}'.format(size_of_a))
    length_of_a = len(a)
    print('\nLength of the matrix: {0}'.format(length_of_a))

    #  4. Resize (crop/slice) matrix A to size (3,4
    a = np.delete(a, [4], axis=1)
    print('\nResize matrix a to (3,4):\n{0}'.format(a))

    #   5. Find the transpose of matrix A and assign it to B
    b = a.transpose()
    print('\nFind the transpose of a and assign to b:\n{0}'.format(b))

    #  6. Find the minimum value in column 1 of matrix B
    b_col1 = np.delete(b, [1, 2], axis=1)  # reshape down to the first column
    print('\nFind the minimum value of column 1 of b: {0}'.format(b_col1.min()))

    #  7. Get the minimum value of the entire matrix
    a_min = a.min()
    print('\nGet the minimum value of the entire matrix a: {0}'.format(a_min))
    a_max = a.max()  # Get the max value of the entire matrix
    print('\nGet the max value of the entire matrix a: {0}'.format(a_max))

    #  8. Create vector X (an array) with 4 random numbers
    x = np.array(random.rand(4))

    #  9. Create a func,on and pass vector X and matrix A in it
    def multiply_vec_matrix(m, v):
        return dot(m, v, out=None)

    #  10. In the new function multiply vector X with matrix A and assign the result to D
    d = multiply_vec_matrix(a, x)

    print('\nCreate a function that multiples vector x with matrix a and assign to d:\n\n{0}\nd = {1}'.format(
        '''def multiply_vec_matrix(m, v):
    return dot(m, v, out=None)\n''', d))

    #  11. Create a complex number Z with absolute and real parts != 0
    z = np.ndarray(shape=(1,1), dtype=complex)
    print('\nCreate complex number z with abs and real parts: {0}'.format(z))
    #  12. Show its real and imaginary parts as well as it’s absolute value
    print('\nShow the real: {0} and imaginary: {1} parts as well as the absolute value {2}'.format(z.real,
                                                                                                   z.imag,
                                                                                                   np.absolute(z)))

    #  13. Multiply result D with the absolute value of Z and record it to C
    c = multiply_vec_matrix(d.transpose(), z.__abs__())
    print('\nMultiply result d with abs value of z:\n{0}'.format(c))

    #  14. Convert matrix B from a matrix to a string and overwrite B
    b = array2string(b)
    print('\nConvert matrix b to a string and overwrite b: {0}\nType of b: {1}'.format(b, type(b)))

    #  15. Display a text on the screen: ‘Your Name is done with HW2‘
    your_name = 'John Blatchford'
    print('\n{0} is done with HW2'.format(your_name))


hw_2()
