from Grid import Grid
from Solution import Solution

if __name__ == '__main__':
    g = Grid()
    #g.create_grid()
    g.testgrid9()
    g.print_ascii_grid()
    # g.print_matplotlib_grid()
    if g.check_validity() is True:
        print("Grid is solvable")
    else:
       print("Grid is not solvable")
    if g.check_validity() is True:
        s = Solution(g)
        s.solve_puzzle(g)
