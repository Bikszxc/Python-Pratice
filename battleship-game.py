import random

class BattleshipGame:
    def __init__(self):
        self.grid_size = 5
        self.attemps = 15
        self.ship_row, self.ship_col = self.set_location()
        self.grid = [[" - " for _ in range(self.grid_size)] for _ in range(self.grid_size)]  # Fixed 5x5 grid
    
    def set_location(self):
        return random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
        
    def display_grid(self):
        for row in self.grid:
            print(" ".join(row))  # Properly prints each row in a single line
                    
    def make_guess(self, row, col):
        if (row, col) == (self.ship_row, self.ship_col):
            print("\nYou sunk the battleship! Sheesh")
            self.grid[row][col] = " 𖦹 "
            return True
        else:
            print("\nBETCH YOU MISSED!")
            self.grid[row][col] = " X "  # Mark the missed shot
            return False
        
    def play(self):
        for attempt in range(self.attemps):
            self.display_grid()
            
            try:
                row, col = map(int, input("Enter row and column (1-5): ").split())
                
                if not (1 <= row <= self.grid_size and 1 <= col <= self.grid_size):
                    print("Invalid Input! Enter numbers between 1 and 5.")
                    continue
                
                row -= 1  # Convert to 0-based index
                col -= 1  # Convert to 0-based index
                
                if self.grid[row][col] != " - ":
                    print("You've already guessed that spot! Try again.")
                    continue
                
                if self.make_guess(row, col):
                    self.display_grid()
                    break   
            except ValueError:
                print("\nPlease enter valid numbers!")
        else:
            print(f"\nGame Over! The ship was at ({self.ship_row + 1}, {self.ship_col + 1}).")
            self.grid[self.ship_row][self.ship_col] = " O "
            self.display_grid()


bg = BattleshipGame()
bg.play()
