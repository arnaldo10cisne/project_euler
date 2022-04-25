import solutions
import json


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
    current_problem.execute_solution()


def run():
    with open('problem_data.json', 'r') as file:
        json_string = file.read()
    data = json.loads(json_string)
    problem = input('What problem would you like to show?: ')
    euler_problem(
        data["data"][f"p{problem}"]["title"],
        data["data"][f"p{problem}"]["description"],
        data["data"][f"p{problem}"]["url"],
        getattr(solutions, f'p{problem}')
    )


if __name__ == "__main__":
    run()
