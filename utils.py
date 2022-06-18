import requests
import os


HTML_TAGS = [
    '<p>', '</p>', '<p class="center">', '<sub>', '</sub>', '<i>',
    '</i>', '<table>', '</table>', '<td>', '</td>', '<tr>', '</tr>',
    '<p class="margin_left">', '<br />', '<sup>', '</sup>'
]


def get_euler_url(min, prob):
    return f'https://projecteuler.net/{"minimal" if min else "problem"}={prob}'


def get_html_text(minimal, problem):
    return requests.get(get_euler_url(minimal, problem)).text


def get_problem_title_from_html(html_text):
    return html_text[html_text.index('<h2>')+4:html_text.index('</h2>')]


def clean_problem_description_format(problem_description):
    for tag in HTML_TAGS:
        problem_description = problem_description.replace(tag, ' ')

    return problem_description


def clear_screen():
    os.system('clear')
