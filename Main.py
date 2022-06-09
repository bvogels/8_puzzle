from Frontend import Frontend
from Grid import Grid
from Solution import Solution


def start_solution(grid, heuristic_choice, goal_state):
    s = Solution(grid, heuristic_choice, goal_state)
    s.solve_puzzle()
    Frontend().statistics(max(s.search_path.keys()), s.count, s.level, s.runtime)


def select_goal_state():
    default_goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    goal_state_grid = default_goal_state
    gstate = Frontend().goal_state()
    if gstate == 1:
        goal_state_grid = default_goal_state
    elif gstate == 2:
        goal_state_grid = Grid().create_random_grid()
    elif gstate == 3:
        goal_state_grid = select_predefined_puzzle()
    elif gstate == 4:
        goal_state_grid = Grid().create_custom_grid()
    return goal_state_grid


def select_predefined_puzzle():
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
    print("List of available states:")
    for index, puzzle in enumerate(grids.values()):
        print(index + 1, ": ", puzzle)
    predefined_grid = grids[int(input("Choose state: "))]
    return predefined_grid


if __name__ == '__main__':
    while True:
        choice = Frontend().main_menu()
        if choice == 1:
            grid = Grid().create_random_grid()
            while Grid().check_validity(grid) is False:
                grid = Grid().create_random_grid()
                Grid().check_validity(grid)
                Grid().print_ascii_grid(grid)
            heuristic_choice = Frontend().choose_heuristic()
            start_solution(grid, heuristic_choice, select_goal_state())
        elif choice == 2:
            grid = Grid().create_custom_grid()
            while Grid().check_validity(grid) is False:
                print(Frontend().messages(2, None))
                grid = Grid().create_custom_grid()
            Grid().print_ascii_grid(grid)
            heuristic_choice = Frontend().choose_heuristic()
            start_solution(grid, heuristic_choice, select_goal_state())
        elif choice == 3:
            grid = select_predefined_puzzle()
            Grid().print_ascii_grid(grid)
            heuristic_choice = Frontend().choose_heuristic()
            start_solution(grid, heuristic_choice, select_goal_state())
        elif choice == 4:
            quit()
