def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    rows = len(m1)
    columns = len(mm2[0])
    multi_matrix = [[0 for i in range(columns)] for j in range(rows)]
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    matrix_one = []
    rows = len(m1)
    columns = len(m1[0])
    add_matrix = [[0 for i in range(columns)] for j in range(rows)]
    for i in range(rows):
        for j in range(columns):
            add_matrix[i][j] = m1[i][j]+m2[i][j]
    return add_matrix


# # def generate_resultant_matrix(rows, columns):
#     add_matrix = [[0*columns]*rows]
#     return add_matrix

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    list_input = input().split(",")
    rows,columns = int(list_input[0]), int(list_input[1])
    for i in range(rows):
        matrix = input().split(" ")
        if len(matrix) == rows:
            matrix.append([int(i) for i in matrix])
    return matrix
        
   
def main():
    # read matrix 1
    matrix_one = read_matrix()
     # read matrix 2
    matrix_two = read_matrix()

    # add matrix 1 and matrix 2

    print(add_matrix(matrix_one,matrix_two))

    # multiply matrix 1 and matrix 2
    
    

if __name__ == '__main__':
    main()
