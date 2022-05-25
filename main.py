from Frontend import Frontend
from Grid import Grid
from Solution import Solution


def start_solution(grid, frontend):
    s = Solution(grid)
    s.solve_puzzle()
    frontend.statistics(max(s.search_path.keys()), s.count, s.level)


grids = {
    1: [[1, 0, 2], [3, 4, 5], [6, 7, 8]],
    2: [[4, 1, 3], [8, 0, 2], [7, 5, 6]],
    3: [[6, 4, 0], [2, 1, 7], [8, 5, 3]],
    4: [[3, 2, 8], [0, 1, 5], [6, 7, 4]],
    5: [[1, 3, 2], [0, 7, 5], [6, 4, 8]],
    6: [[7, 4, 6], [1, 3, 5], [8, 0, 2]],
    7: [[4, 7, 0], [8, 5, 3], [2, 6, 1]],
    8: [[5, 1, 2], [4, 8, 0], [3, 6, 7]],
    9: [[2, 1, 7], [8, 3, 6], [5, 4, 0]],
    10: [[3, 5, 8], [1, 7, 0], [6, 4, 2]]
}

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
        elif choice == 2:
            print(f.messages(1, None))
            numbers = input("Grid: ")
            g = Grid()
            if g.create_custom_grid(numbers, f) is True:
                start_solution(g, f)
        elif choice == 3:
            print("List of puzzles:")
            for index, puzzle in enumerate(grids.values()):
                print(index + 1, ": ", puzzle)
            grid = grids[int(input("Choose puzzle: "))]
            g = Grid()
            g.grid = grid
            start_solution(g, f)
        elif choice == 4:
            quit()
