import requests
import os


HTML_TAGS = [
    '<p>', '</p>', '<p class="center">', '<sub>', '</sub>', '<i>',
    '</i>', '<table>', '</table>', '<td>', '</td>', '<tr>', '</tr>',
    '<p class="margin_left">', '<br />', '<sup>', '</sup>'
]


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


def get_euler_url(min, prob):
    return f'https://projecteuler.net/{"minimal" if min else "problem"}={prob}'


def get_html_text(minimal, problem):
    return requests.get(get_euler_url(minimal, problem)).text


def get_problem_title_from_html(html_text):
    return html_text[html_text.index('<h2>')+4:html_text.index('</h2>')]+'\n'


def clean_problem_description_format(problem_description):
    for tag in HTML_TAGS:
        problem_description = problem_description.replace(tag, ' ')

    return problem_description


def clear_screen():
    os.system('clear')


def euler_problem(title, description, url, solution_method):
    current_problem = EulerProblem(title, description, url, solution_method)
    current_problem.show_title()
    current_problem.show_description()
    if solution_method is not None:
        current_problem.execute_solution()
