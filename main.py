from Frontend import Frontend
from Grid import Grid
from Solution import Solution


def start_solution(grid, frontend):
    s = Solution(grid)
    s.solve_puzzle(grid)
    frontend.statistics(max(s.search_path.keys()), s.paths, s.count)


if __name__ == '__main__':
    f = Frontend()
    while True:
        choice = f.main_menu()
        if choice == 1:
            g = Grid()
            g.create_random_grid()
            while g.check_validity() is False:
                g.create_random_grid()
                g.check_validity()
                g.print_ascii_grid()
            start_solution(g, f)
            quit()
        elif choice == 2:
            print(f.messages(1, None))
            numbers = input("Grid: ")
            g = Grid()
            if g.create_custom_grid(numbers, f) is True:
                start_solution(g, f)

        # g.print_matplotlib_grid()
        # if g.check_validity() is True:
        #    print("Grid is solvable")
        # else:
        #   print("Grid is not solvable")
        # if g.check_validity() is True:
