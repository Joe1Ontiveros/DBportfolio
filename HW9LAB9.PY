import numpy as np
import sympy as sp
from sympy import Matrix

# def get_inverse(matrix):
#     try:
#         inverse_matrix = np.linalg.inv(matrix)
#         return inverse_matrix
#     except np.linalg.LinAlgError:
#         return "Matrix is singular and cannot be inverted."

# # Example usage
# pe = np.array([[1,1,1],[-1,1,1],[0,2,-3]])
# inverse_pe = get_inverse(pe)
# print("Inverse of matrix pe:")
# print(inverse_pe)

# # Display in fraction form

# pe_sympy = Matrix(pe)
# inverse_pe_sympy = pe_sympy.inv()
# print("Inverse of matrix pe in fraction form:")
# print(inverse_pe_sympy)

def solve_example_a():
    # Let's assume S₂ = {v₁, v₂, v₃} and we have the transition matrix from S to S₂
    # If P is the transition matrix from S = {w₁, w₂, w₃} to S₂ = {v₁, v₂, v₃}
    
    # This is just a placeholder - you'll need to replace with actual values
# Using NumPy with floating-point approximations
    s6 = [
        Matrix([1/2,1/2,1/2,1/2]),
        Matrix([1/2, 1/2, -1/2, -1/2]),
        Matrix([1/2, -1/2, 1/2, -1/2]),
        Matrix([1/2, -1/2, -1/2, 1/2])
    ]
    P = Matrix.hstack(*s6)  

    import numpy as np

    P= Matrix([
       [-1,4],
       [1,-3]
    ])
    Ei = Matrix([
        [2,0],
        [0,1]
    ])
    0
    # p
    # A = Matrix([
    #    [1,0,0,0],
    #    [0,2,0,0],
    #    [0,0,0,0],
    #    [0,0,0,4]
    # ])
    # # Define matrix P
    # P = Matrix([
    #     [1/2, 1/2, 1/2,1/2],
    #     [1/2,1/2,-1/2,-1/2],
    #     [1/2,-1/2,1/2,-1/2],
    #     [1/2,-1/2,-1/2,1/2]
    # ])

    # Compute the inverse of P
    P_inv = P.inv()
    print('inveres of P: ',P_inv)
    result = P_inv * Ei * P
    print("QUESTION 4 D: ")
    result_list = result.tolist()
    for row in result_list:
        print(" ".join(f"{elem:8.2f}" for elem in row))

    # P = Matrix([
    #     [1, 2, -4],
    #     [-3, -3, 4],
    #     [1, 1, -1]
    # ])
    # Using SymPy for exact symbolic representation
    S3_sympy = Matrix([
        [np.sqrt(3)/3, np.sqrt(2)/2, -np.sqrt(6)/6],
        [np.sqrt(3)/3, 0, np.sqrt(6)/3],
        [np.sqrt(3)/3, -np.sqrt(2)/2, -np.sqrt(6)/6]
    ])
 # Define the vectors we need to find coordinates for
    v1 = Matrix([1, 0, 0])
    v2 = Matrix([0, 1, 0])
    v3 = Matrix([0, 0, 1])

    # Stack the vectors to solve for all simultaneously
    v = Matrix.hstack(v1, v2, v3)
    X1 = Matrix([1, 2, -4])
    X2 = Matrix([-3, -3, 4])
    X3 = Matrix([1, 1, 1 ])   
    X = Matrix.hstack(X1,X2,X3)
    # The coordinates of v in basis S would be:
    coordinates = S3_sympy.inv() * X
    
    P1 = Matrix([1, 0, 0,0])
    P2 = Matrix([-1,-2,0,0])
    P3 = Matrix([1, 1, 1,0 ])  
    P4 = Matrix([0, 1, 1,-2 ])     
    P = Matrix.hstack(P1,P2,P3,P4)  
    # coordinates = X * P
    # print("Coordinates of v = (1, 1, 1) in basis S:")
    # # print(v_in_S)
    # # print(coordinates)
    # # Extract the coordinates for each vector
    # v1_coordinates = coordinates.col(0).applyfunc(lambda x: round(x, 2))
    # print("Coordinates of v1 in basis S:")
    # print(v1_coordinates)
    # v2_coordinates = coordinates.col(1).applyfunc(lambda x: round(x, 2))
    # print("Coordinates of v2 in basis S:")
    # print(v2_coordinates)
    # v3_coordinates = coordinates.col(2).applyfunc(lambda x: round(x, 2))
    # print("Coordinates of v3 in basis S:")
    # print(v3_coordinates)

# solve_example_a()


def problem7():
    # Define the matrix A using SymPy
    A_sp = Matrix([
        [-3, -5, -2],
        [-5, 0, -5],
        [-2, -5, -3]
    ])

    # 1. Find eigenvalues and eigenvectors using SymPy
    eigenvals = A_sp.eigenvals()
    eigenvects = A_sp.eigenvects()

    print("Eigenvalues (SymPy):", eigenvals)
    print("Eigenvectors (SymPy):", eigenvects)

    P_sp = sp.Matrix([
        eigenvects[0][2][0],
        eigenvects[1][2][0],
        eigenvects[2][2][0]
    ])
    D_sp = sp.diag(*eigenvals.keys())

    print("Matrix P (SymPy):")
    print(P_sp)
    print("Matrix D (SymPy):")
    print(D_sp)
    
    
    
def problem1():
    S_2 = Matrix([
        [1,-3,1],
        [2,-3,1],
        [-4,4,-1]
    ])

    # Compute the reduced row echelon form (rref) of S_2
    S_2_rref, pivot_columns = S_2.rref()
    

    # Display the rref of S_2
    print("Reduced Row Echelon Form (rref) of S_2:")
    sp.pprint(S_2_rref)
    # Define the augmented matrix [S_2 | (1, 1, 1)]
    augmented_matrix = S_2.row_join(Matrix([1, 1, 1]))

    # Compute the reduced row echelon form (rref) of the augmented matrix
    augmented_rref, pivot_columns = augmented_matrix.rref()

    # Display the rref of -the augmented matrix
    print("Reduced Row Echelon Form (rref) of the augmented matrix [S_2 | (1, 1, 1)]:")
    sp.pprint(augmented_rref)

problem7()
# problem1()