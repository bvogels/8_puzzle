from Frontend import Frontend
from Grid import Grid
from Solution import Solution

if __name__ == '__main__':
    f = Frontend()
    choice = f.main_menu()
    if choice == 1:
        g = Grid()
        g.create_random_grid()
        #while g.check_validity() is True:
        #    g.create_grid()
        #    g.check_validity()
        #    g.print_ascii_grid()
        s = Solution(g)
        s.solve_puzzle(g)
    elif choice == 2:
        print(f.messages(1, None))
        numbers = input("Grid: ")
        g = Grid()
        g.create_custom_grid(numbers, f)
        s = Solution(g)
        s.solve_puzzle(g)
    # g.print_matplotlib_grid()
    #if g.check_validity() is True:
    #    print("Grid is solvable")
    #else:
    #   print("Grid is not solvable")
    #if g.check_validity() is True:

