class KnightsTour:
    def __init__(self, board_size=8):
        """
        Initialize the Knight's Tour solver.
        
        :param board_size: Size of the chessboard (default is 8x8)
        """
        self.board_size = board_size
        self.moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
    
    def is_valid_move(self, board, x, y):
        """
        Check if the move is valid and the square has not been visited.
        
        :param board: Current state of the board
        :param x: x-coordinate of the move
        :param y: y-coordinate of the move
        :return: Boolean indicating if the move is valid
        """
        return (0 <= x < self.board_size and 
                0 <= y < self.board_size and 
                board[x][y] == -1)
    
    def solve(self, start_x, start_y):
        """
        Solve the Knight's Tour starting from the given position.
        
        :param start_x: Starting x-coordinate
        :param start_y: Starting y-coordinate
        :return: A 2D list representing the order of moves, or None if no solution
        """
        # Validate start position
        if not (0 <= start_x < self.board_size and 0 <= start_y < self.board_size):
            raise ValueError("Start position is outside the board")
        
        # Initialize board with -1 (unvisited)
        board = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]
        
        # First move
        board[start_x][start_y] = 0
        
        # Try to solve the tour
        if self._solve_tour(board, start_x, start_y, 1):
            return board
        
        return None
    
    def _solve_tour(self, board, current_x, current_y, move_count):
        """
        Recursive backtracking method to solve the Knight's Tour.
        
        :param board: Current state of the board
        :param current_x: Current x-coordinate
        :param current_y: Current y-coordinate
        :param move_count: Number of moves made so far
        :return: Boolean indicating if a complete tour is possible
        """
        # If all squares have been visited, tour is complete
        if move_count == self.board_size * self.board_size:
            return True
        
        # Try all possible knight moves
        for dx, dy in self.moves:
            next_x, next_y = current_x + dx, current_y + dy
            
            # Check if the move is valid
            if self.is_valid_move(board, next_x, next_y):
                # Mark the square with current move number
                board[next_x][next_y] = move_count
                
                # Recursively try to complete the tour
                if self._solve_tour(board, next_x, next_y, move_count + 1):
                    return True
                
                # Backtrack if the move doesn't lead to a solution
                board[next_x][next_y] = -1
        
        return False