import random
###import matplotlib.pyplot as plt
from Frontend import Frontend


class Grid:
    grid = [[], [], []]

    ###
    ###### Create a 3x3 puzzle with the numbers 0 to 8
    #########
    ######
    ###

    def create_grid(self, numbers):
        r, e = 0, 0
        while r < 3:
            c = 0
            while c < 3:
                self.grid[r].append(numbers[e])
                c += 1
                e += 1
            r += 1

    def create_random_grid(self):
        numbers = [n for n in range(0, 9)]
        random.shuffle(numbers)
        self.create_grid(numbers)

    def create_custom_grid(self, numbers):
        if len(numbers) == 9:
            numbers = [int(n) for n in list(numbers)]
            if len(set(numbers)) == len(numbers) and min(numbers) == 0 and max(numbers) == 8:
                self.create_grid(numbers)
                return True
            else:
                print(Frontend().messages(3, None))
                return False
        else:
            print(Frontend().messages(4, None))
            return False

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
