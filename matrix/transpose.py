def transpose(matrix):
    # Get the dimensions of the original array
    num_rows= len(matrix)
    num_cols= len(matrix[0]) if num_rows > 0 else 0

    # Create an empty matrix for the transposed matrix  
    transposed = []

    # Fill the transposed matrix with zeros
    for _ in range(num_cols):
        transposed.append([0] * num_rows)
        
    # Fill the transposed matrix by exchanging rows for columns
    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed 
    
     
