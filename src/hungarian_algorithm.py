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
    working_matrix = matrix.copy()
    
    # Step 1: Subtract row minimums (reduce matrix)
    for i in range(n):
        working_matrix[i] -= working_matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(n):
        working_matrix[:, j] -= working_matrix[:, j].min()
    
    # Find optimal assignments
    def find_assignments(matrix):
        # Track which rows and columns are covered
        covered_rows = [False] * n
        covered_cols = [False] * n
        
        # To store optimal assignments
        assignments = [-1] * n
        
        # Find initial zero assignments
        for i in range(n):
            for j in range(n):
                if matrix[i, j] == 0 and not covered_rows[i] and not covered_cols[j]:
                    assignments[i] = j
                    covered_rows[i] = True
                    covered_cols[j] = True
        
        return assignments
    
    # Find the optimal assignments
    assignments = find_assignments(working_matrix)
    
    # Compute total cost based on original cost matrix
    total_cost = sum(cost_matrix[i][assignments[i]] for i in range(n))
    
    return assignments, total_cost