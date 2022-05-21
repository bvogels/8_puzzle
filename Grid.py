import random
import matplotlib.pyplot as plt





class Grid:
    grid = [[], [], []]

    ###
    ###### Create a 3x3 puzzle with the numbers 0 to 8
    #########
    ######
    ###

    def create_grid(self):
        r, e = 0, 0
        numbers = [n for n in range(0, 9)]
        random.shuffle(numbers)
        while r < 3:
            c = 0
            while c < 3:
                self.grid[r].append(numbers[e])
                c += 1
                e += 1
            r += 1
        print(self.grid)

    ###
    ###### Check if the puzzle is even solvable.
    #########
    ######
    ###

    def check_validity(self):
        shifts = 0  # The number of tile shifts
        flat_grid = sum(self.grid, [])  # flatten the grid -> This is only necessary no make coding less painful
        flat_grid.remove(0)  # Remove the 0 value

        # Traverse the grid to search for misplaced tiles.
        for e in flat_grid:
            for n in range(flat_grid.index(e), e):
                if e > flat_grid[n]:
                    shifts += 1
        if shifts % 2 == 0:
            return True
        else:
            return False

    ###
    ###### Print a grid to display the puzzle in the terminal
    #########
    ######
    ###

    def print_ascii_grid(self):
        print("+---" * 3 + "+")
        print("|", self.grid[0][0], "|", self.grid[0][1], "|", self.grid[0][2], "|", )
        print("+---" * 3 + "+")
        print("|", self.grid[1][0], "|", self.grid[1][1], "|", self.grid[1][2], "|", )
        print("+---" * 3 + "+")
        print("|", self.grid[2][0], "|", self.grid[2][1], "|", self.grid[2][2], "|", )
        print("+---" * 3 + "+")

    ###
    ###### Print the grid in a very rudimentary matplotlib display
    #########
    ######
    ###

    def print_matplotlib_grid(self):
        y = 1
        fig, ax = plt.subplots()
        ax.grid(which='major', color='black', linestyle='', linewidth=1)
        ax.set_xlim([0, 3])
        ax.set_ylim([0, 3])
        for e in reversed(self.grid):
            x = 1
            n = 0
            while n < 3:
                ax.text(x - 0.5, y - 0.5, e[n], ha='center', va='center')
                x += 1
                n += 1
            y += 1
        plt.show()
