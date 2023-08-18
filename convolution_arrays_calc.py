import numpy as np


def calc_convolution_matrix(input_matrix, kernel):
    """
    This function calculates a simple convolutional matrix from in_matrix
    applying a kernel matrix and returns a Numpy ndarray
    --keyword arguments--
    in_matrix: NumPy ndarray
    kernel: NumPy ndarray

    """
    # a kernel's dimension
    k_height = kernel.shape[0]
    k_width = kernel.shape[1]

    # output matrix dimension
    output_height = input_matrix.shape[0] - k_height + 1
    output_width = input_matrix.shape[1] - k_width + 1

    # create empty matrix
    output_matrix = np.zeros((output_height, output_width))

    # calculate matrix
    for i in range(0, output_height):
        for j in range(0, output_width):
            for ii in range(0, kernel.shape[0]):
                for jj in range(0, kernel.shape[1]):
                    output_matrix[i, j] += np.sum((
                        np.multiply(input_matrix[i + ii, j + jj], kernel[ii, jj])))

    return output_matrix


