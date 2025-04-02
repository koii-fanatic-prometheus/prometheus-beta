import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm.
    
    The Hungarian algorithm finds the optimal assignment that minimizes the total cost.
    
    Args:
        cost_matrix (list or np.ndarray): A square matrix representing costs of assignments.
                                          Each element cost_matrix[i][j] represents the cost 
                                          of assigning worker i to task j.
    
    Returns:
        tuple: A tuple containing:
            - optimal_assignments (list): List of assigned tasks for each worker
            - total_cost (float): Total cost of the optimal assignment
    
    Raises:
        ValueError: If the input is not a valid square matrix
    """
    # Convert input to numpy array for consistent processing
    matrix = np.array(cost_matrix, dtype=float)
    
    # Validate input
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input must be a square matrix")
    
    n = matrix.shape[0]
    
    # Step 1: Subtract row minimums (reduce matrix)
    for i in range(n):
        matrix[i] -= matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(n):
        matrix[:, j] -= matrix[:, j].min()
    
    def find_minimum_lines(matrix):
        """Find the minimum number of lines to cover all zeros"""
        # Use a greedy approach to mark rows and columns
        n = matrix.shape[0]
        row_covered = [False] * n
        col_covered = [False] * n
        
        zero_lines = 0
        assignments = [-1] * n
        
        # Find independent zero assignments
        for i in range(n):
            for j in range(n):
                if matrix[i, j] == 0 and not row_covered[i] and not col_covered[j]:
                    assignments[i] = j
                    row_covered[i] = True
                    col_covered[j] = True
                    zero_lines += 1
        
        return assignments, zero_lines
    
    # Initial attempt to find optimal assignments
    assignments, lines = find_minimum_lines(matrix)
    
    # If not all tasks are assigned, adjust the matrix
    while lines < n:
        # Find the smallest uncovered element
        min_uncovered = float('inf')
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if not (row_covered[i] or col_covered[j]):
                    min_uncovered = min(min_uncovered, matrix[i, j])
        
        # Modify matrix
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if row_covered[i]:
                    matrix[i, j] += min_uncovered
                if not col_covered[j]:
                    matrix[i, j] -= min_uncovered
        
        # Reattempt finding assignments
        assignments, lines = find_minimum_lines(matrix)
    
    # Calculate total cost of the optimal assignment
    total_cost = sum(cost_matrix[i][assignments[i]] for i in range(n))
    
    return assignments, total_cost