def tower_of_hanoi(n, source='A', auxiliary='B', destination='C'):
    """
    Solve the Tower of Hanoi puzzle recursively.
    
    Args:
        n (int): Number of disks to move (must be positive)
        source (str): Name of the source rod (default 'A')
        auxiliary (str): Name of the auxiliary rod (default 'B')
        destination (str): Name of the destination rod (default 'C')
    
    Returns:
        list: A list of move tuples, each representing a disk move
    
    Raises:
        ValueError: If number of disks is not a positive integer
    """
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Number of disks must be a non-negative integer")
    
    # Base case: no disks to move
    if n == 0:
        return []
    
    # Recursive solution for moving n disks
    moves = []
    
    # Move n-1 disks from source to auxiliary rod
    moves.extend(tower_of_hanoi(n-1, source, destination, auxiliary))
    
    # Move the nth (largest) disk from source to destination
    moves.append((source, destination))
    
    # Move n-1 disks from auxiliary to destination rod
    moves.extend(tower_of_hanoi(n-1, auxiliary, source, destination))
    
    return moves

def print_tower_of_hanoi_moves(n, source='A', auxiliary='B', destination='C'):
    """
    Print the moves to solve the Tower of Hanoi puzzle.
    
    Args:
        n (int): Number of disks to move
        source (str): Name of the source rod (default 'A')
        auxiliary (str): Name of the auxiliary rod (default 'B')
        destination (str): Name of the destination rod (default 'C')
    
    Prints the sequence of moves to solve the puzzle
    """
    moves = tower_of_hanoi(n, source, auxiliary, destination)
    for move in moves:
        print(f"Move disk from {move[0]} to {move[1]}")