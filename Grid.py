import copy
import random
###import matplotlib.pyplot as plt
from Frontend import Frontend


class Grid:

    ###
    ###### Create a 3x3 puzzle with the numbers 0 to 8
    #########
    ######
    ###

    def create_grid(self, numbers):
        grid = [[], [], []]
        r, e = 0, 0
        while r < 3:
            c = 0
            while c < 3:
                grid[r].append(numbers[e])
                c += 1
                e += 1
            r += 1
        return grid

    def create_random_grid(self):
        numbers = [n for n in range(0, 9)]
        random.shuffle(numbers)
        while self.check_validity(numbers) is False:
            numbers = [n for n in range(0, 9)]
            random.shuffle(numbers)
        grid = self.create_grid(numbers)
        return grid


    def create_custom_grid(self):
        print(Frontend().messages(1, None))
        numbers = input("Grid: ")
        if len(numbers) == 9:
            numbers = [int(n) for n in list(numbers)]
            if len(set(numbers)) == len(numbers) and min(numbers) == 0 and max(numbers) == 8:
                if self.check_validity(numbers):
                    return self.create_grid(numbers)
                else:
                    print(Frontend().messages(2, None))
                    self.create_custom_grid()
            else:
                print(Frontend().messages(3, None))
                self.create_custom_grid()
        else:
            print(Frontend().messages(4, None))
            self.create_custom_grid()

    ###
    ###### Check if the puzzle is even solvable.
    #########
    ######
    ###

    def check_validity(self, flat_grid):
        shifts = 0  # The number of tile shifts
        #flat_grid.remove(0)  # Remove the 0 value

        # Traverse the grid to search for misplaced tiles.
        for e in flat_grid:
            for n in range(flat_grid.index(e), e):
                if e > flat_grid[n]:# and flat_grid[n] != 0 and flat_grid[e] != 0:
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

    def print_ascii_grid(self, grid):
        print("+---" * 3 + "+")
        print("|", grid[0][0], "|", grid[0][1], "|", grid[0][2], "|", )
        print("+---" * 3 + "+")
        print("|", grid[1][0], "|", grid[1][1], "|", grid[1][2], "|", )
        print("+---" * 3 + "+")
        print("|", grid[2][0], "|", grid[2][1], "|", grid[2][2], "|", )
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
