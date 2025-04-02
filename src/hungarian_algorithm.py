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
    
    # Step 3: Cover zeros with minimum number of lines
    def cover_zeros(matrix):
        # Create boolean arrays to track covered rows and columns
        covered_rows = [False] * n
        covered_cols = [False] * n
        
        # Count lines needed to cover all zeros
        lines = 0
        
        # Find independent zeros
        assignments = [-1] * n
        for i in range(n):
            for j in range(n):
                if matrix[i, j] == 0 and not covered_rows[i] and not covered_cols[j]:
                    assignments[i] = j
                    covered_rows[i] = True
                    covered_cols[j] = True
                    lines += 1
        
        return assignments, lines
    
    # Step 4: Adjust matrix if needed
    assignments, lines = cover_zeros(matrix)
    
    while lines < n:
        # Find the smallest uncovered element
        min_uncovered = float('inf')
        for i in range(n):
            for j in range(n):
                if not (covered_rows[i] or covered_cols[j]):
                    min_uncovered = min(min_uncovered, matrix[i, j])
        
        # Adjust matrix
        for i in range(n):
            for j in range(n):
                if covered_rows[i]:
                    matrix[i, j] += min_uncovered
                if not covered_cols[j]:
                    matrix[i, j] -= min_uncovered
        
        # Recheck assignments
        assignments, lines = cover_zeros(matrix)
    
    # Calculate total cost of the optimal assignment
    total_cost = sum(cost_matrix[i][assignments[i]] for i in range(n))
    
    return assignments, total_cost