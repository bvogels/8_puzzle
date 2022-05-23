import random
import matplotlib.pyplot as plt


class Grid:
    grid = [[], [], []]

    ###
    ###### Create a 3x3 puzzle with the numbers 0 to 8
    #########
    ######
    ###

    def testgrid1(self):
        self.grid = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]

    def testgrid2(self):
        self.grid = [[4, 1, 3], [8, 0, 2], [7, 5, 6]]

    def testgrid3(self):
        self.grid = [[6, 4, 0], [2, 1, 7], [8, 5, 3]]

    def testgrid4(self):
        self.grid = [[3, 2, 8], [0, 1, 5], [6, 7, 4]]

    def testgrid5(self):
        self.grid = [[1, 3, 2], [0, 7, 5], [6, 4, 8]]

    def testgrid6(self):
        self.grid = [[7, 4, 6], [1, 3, 5], [8, 0, 2]]

    def testgrid7(self):
        self.grid = [[4, 7, 0], [8, 5, 3], [2, 6, 1]]

    def testgrid8(self):
        self.grid = [[5, 1, 2], [4, 8, 0], [3, 6, 7]]

    def testgrid9(self):
        self.grid = [[2, 1, 7], [8, 3, 6], [5, 4, 0]]

    def create_grid(self, numbers):
        r, e = 0, 0
        while r < 3:
            c = 0
            while c < 3:
                self.grid[r].append(numbers[e])
                c += 1
                e += 1
            r += 1
        print(self.grid)

    def create_random_grid(self):
        numbers = [n for n in range(0, 9)]
        random.shuffle(numbers)
        self.create_grid(numbers)

    def create_custom_grid(self, numbers, frontend):
        if len(numbers) == 9:
            numbers = [int(n) for n in list(numbers)]
            if len(set(numbers)) == len(numbers) and min(numbers) == 0 and max(numbers) == 8:
                self.create_grid(numbers)
            else:
                print(frontend.messages(3, None))
                frontend.main_menu()
        else:
            print(frontend.messages(4, None))
        frontend.main_menu()



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
