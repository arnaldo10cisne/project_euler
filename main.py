import solutions
from utils import (
    clear_screen,
    get_problem_title_from_html,
    get_html_text,
    clean_problem_description_format
)


class EulerProblem():
    def __init__(self, title, description, url, solution_method):
        self.title = title
        self.description = description
        self.url = url
        self.solution_method = solution_method

    def show_title(self):
        print(self.title)

    def show_description(self):
        print(self.description)

    def execute_solution(self):
        self.solution_method()


def euler_problem(title, description, url, solution_method):
    current_problem = EulerProblem(title, description, url, solution_method)
    current_problem.show_title()
    current_problem.show_description()
    if solution_method is not None:
        current_problem.execute_solution()


def run():
    while True:
        clear_screen()
        problem = input('Number of problem to show (Press 0 to exit): ')
        clear_screen()
        if problem == '0':
            break

        euler_problem(
            get_problem_title_from_html(get_html_text(False, problem))+'\n',
            clean_problem_description_format(get_html_text(True, problem)),
            f"https://projecteuler.net/problem={problem}",
            getattr(solutions, f'p{problem}', None)
        )
        print('\nPress enter to continue\n')
        input('')


if __name__ == "__main__":
    run()
