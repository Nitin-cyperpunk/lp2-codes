class NQueens: 
    def __init__(self, n): 
        self.n = n 
        self.board = [-1] * n  # Stores column positions for queens in each row 
        self.count = 0 
    def is_safe(self, row, col): 
        for r in range(row): 
            if self.board[r] == col or abs(self.board[r] - col) == abs(r - row): 
                return False 
        return True  
    def solve(self, row=0): 
        if row == self.n: 
            self.count += 1 
            self.print_board() 
            return 
        for col in range(self.n): 
            if self.is_safe(row, col): 
                self.board[row] = col 
                self.solve(row + 1) 
    def print_board(self): 
        for r in range(self.n): 
            print(" ".join("Q" if c == self.board[r] else "X" for c in range(self.n))) 
        print() 
if __name__ == "__main__": 
    n = int(input("Enter board size: ")) 
    solver = NQueens(n) 
    solver.solve() 
    print(f"Total solutions: {solver.count}") 