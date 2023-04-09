#!/usr/bin/env python3
# Filename: get_problem.py

"""Fetch a problem from Project Euler and set up a python file in the problems
folder to contain the solution"""

import click
import requests
from bs4 import BeautifulSoup


@click.command()
@click.option("--problem", help="Project Euler problem number")
def create_problem_template(problem):
    """Read the list of problems available on project euler and fetch the specified problem"""
    # Fetch the problem HTML data
    resp = requests.get(f"https://projecteuler.net/problem={problem}")
    # Parse the HTML response as beautiful soup
    soup = BeautifulSoup(resp.text, features="html.parser")

    problem_title = soup.find("h2").text.strip()
    problem_number = soup.find("h3").text.strip()
    problem_task = soup.find("div", {"class": "problem_content"}).get_text().strip()

    with open(f"./problems/problem_{problem}.py", "w") as f:
        f.write(
            f"""#!/usr/bin/env python3
# Filename: problem_{problem}.py
\"\"\"
{problem_number}
{problem_title}
{problem_task}
\"\"\"

import time

def problem_{problem}():
    # Solution Here

if __name__ == "__main__":
    start_time = time.time()
    result = problem_{problem}()
    end_time = time.time()

    print(f"The answer is {{result:,}}.")
    print(f"The the solution took {{end_time-start_time:0.2}} seconds.")
""")



if __name__ == "__main__":
    create_problem_template()
