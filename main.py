import solutions
from utils import (
    clear_screen,
    get_problem_title_from_html,
    get_html_text,
    clean_problem_description_format,
    euler_problem
)


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
